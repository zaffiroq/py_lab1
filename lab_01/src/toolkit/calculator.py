from dataclasses import dataclass

from toolkit.errors import (
    DivisionByZeroError,
    DoubleBinaryOperandError,
    EmptyExpressionError,
    InappropriateSymbolError,
    InvalidNumberError,
    MissedOperandError,
)


@dataclass
class Token:
    kind: str
    value: float | str

priority = {"+": 1, "-": 1, "*": 2, "/": 2}


def tokenization(expression:str):

    tokens = []
    i = 0
    n = len(expression)

    while i < n:
        if expression[i] == ' ':
            i += 1
            continue
        if expression[i].isdigit() or expression[i] == '.':
            start = i
            dot = 0
            while i < n and (expression[i].isdigit() or expression[i] == '.') and dot <= 1:
                if expression[i] == '.':
                    dot += 1
                    if dot > 1:
                        raise InvalidNumberError(expression[start : i + 1])
                i += 1

            token = expression[start:i]

            if token == '.':
                raise InvalidNumberError(token)
            tokens.append(Token('number', float(token)))
            continue

        if expression[i] in '+-*/':
            tokens.append(Token('operand', expression[i]))
            i += 1
            continue
        if expression[i].isdigit() == False or expression[i] not in '+-*/':
            raise InappropriateSymbolError(expression[i])

    if len(tokens) == 0:
        raise EmptyExpressionError
    return tokens


def validation(tokens):

    if tokens[0].kind == 'operand' and tokens[0].value not in '+-':
        raise MissedOperandError()

    if tokens[-1].kind != 'number':
        raise MissedOperandError()

    for token_id in range(1, len(tokens)):
        prev, cur = tokens[token_id - 1], tokens[token_id]

        if prev.kind == 'number' and cur.kind == 'number':
            raise MissedOperandError()

        if prev.kind == 'operand' and cur.kind == 'operand':

            if cur.value not in '+-':
                raise DoubleBinaryOperandError(prev.value, cur.value)

            nxt = tokens[token_id + 1] if token_id + 1 < len(tokens) else None
            if nxt is None or nxt.kind != 'number':
                raise MissedOperandError()

    return tokens

def unary(tokens):
    pending_sign = 1
    result = []
    for token_id, token in enumerate(tokens):
        if (token.kind == 'operand' and token.value in '+-' and (
            token_id == 0 or tokens[token_id - 1].kind == 'operand')):
            if token.value == "-":
                pending_sign *= -1
        elif token.kind == 'number':
            result.append(Token('number', token.value * pending_sign))
            pending_sign = 1
        else:
            result.append(token)

    return result

def RPN(tokens):
    stack = []
    rpn_output = []

    for token in tokens:

        if token.kind == 'number':
            rpn_output.append(token)

        else:
            while len(stack) > 0 and priority[stack[-1].value] >= priority[token.value]:
                rpn_output.append(stack.pop())
            stack.append(token)

    while len(stack) > 0:
        rpn_output.append(stack.pop())

    return rpn_output

def evaluation(rpn_output):

    stack = []

    for token in rpn_output:

        if token.kind == 'number':
            stack.append(token.value)

        else:
            b = stack.pop()
            a = stack.pop()
            if token.value == "+":
                stack.append(a + b)

            elif token.value == "-":
                stack.append(a - b)

            elif token.value == "*":
                stack.append(a * b)

            else:
                if b == 0:
                    raise DivisionByZeroError()
                stack.append(a / b)

    return stack[0]

def calculate(expression):

    tokens = tokenization(expression)
    tokens = validation(tokens)
    tokens = unary(tokens)
    return evaluation(RPN(tokens))












