from dataclasses import dataclass
from toolkit.errors import(
EmptyExpressionError,
MissedOperandError,
InvalidNumberError,
InappropriateSymbolError,
DoubleBinaryOperandError,
DivisionByZeroError
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
        character = expression[i]
        if character == ' ':
            i += 1
            continue
        if character.isdigit() or character == '.':
            start = i
            dot = 0
            while i < n and (character.isdigit() or character == '.') and dot <= 1:
                if character == '.':
                    dot += 1
                    if dot > 1:
                        raise InvalidNumberError
                i += 1

            token = expression[start:i]

            if token == '.':
                raise InvalidNumberError
            tokens.append(Token('number',str(token)))

        if character in '+-*/':
            tokens.append([character, 'operand'])
            i += 1
            continue
        if character.isdigit() == False or character not in '+-*/':
            raise InappropriateSymbolError

    if len(tokens) == 0:
        raise EmptyExpressionError
    return tokens


def validation(tokens):

    if tokens[0].kind == 'operand' and tokens[0].value not in '+-':
        raise MissedOperandError()

    if tokens[-1].kind != 'number':
        raise MissedOperandError()

    for token_id in range(1,len(tokens)):

        if tokens[token_id].kind == 'number' and tokens[token_id+1].kind == 'number':
            raise MissedOperandError()

        if tokens[token_id].kind == 'operand' and tokens[token_id+1].kind == 'operand':
            if tokens[token_id + 1].value not in '+-':
                raise DoubleBinaryOperandError(str(tokens[token_id].value),str(tokens[token_id+1].value))

        if (token_id + 2) < len(tokens):
            if tokens[token_id+2].kind != 'number':
                raise MissedOperandError()

def unary(tokens):
    pending_sign = 1
    result = []
    for token_id, token in enumerate(tokens):
        if (token.kind == 'operand' and token.value in '+-' and (
            token_id == 0 or tokens[token_id - 1].kind == 'operand')):
            if token.value == "-":
                pending_sign *= -1
        elif token.kind == 'number':
            result.append(Token(token.value * pending_sign,'number'))
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
    while len(rpn_output) > 1:
        i = 0
        if rpn_output[i].kind == 'number':
            i += 1
        elif rpn_output[i].kind == 'operand':

            if rpn_output[i].value == '+':
                rpn_output[i] = Token('number', rpn_output[i-2].value + rpn_output[i-1].value)

            elif rpn_output[i].value == '-':
                rpn_output[i] = Token('number', rpn_output[i-2].value + rpn_output[i-1].value)

            elif rpn_output[i].value == '*':
                rpn_output[i] = Token('number', rpn_output[i-2].value + rpn_output[i-1].value)

            elif rpn_output[i].value == '/':
                if rpn_output[-1].value == 0:
                    raise DivisionByZeroError()
                else:
                    rpn_output[i] = Token('number', rpn_output[i-2].value + rpn_output[i-1].value)


            rpn_output.pop(i - 2)
            rpn_output.pop(i - 2)

        return rpn_output

def calculate(expression):

    tokens = tokenization(expression)
    tokens = validation(tokens)
    tokens = unary(tokens)
    return evaluation(RPN(tokens))















