class Error(Exception):
    pass
class EmptyExpressionError(Error):
    def __init__(self) -> None:
        super().__init__("Пустое выражение")

class InappropriateSymbolError(Error):
    def __init__(self,symbol: str) -> None:
        super().__init__(f"Недопустимый символ: {symbol!r}")
class InvalidNumberError(Error):
    def __init__(self, number: str) -> None:
        super().__init__(f"Некорректное число : {number!r}")

class MissedOperandError(Error):
    def __init__(self) -> None:
        super().__init__("Пропущенный операнд")

class DoubleBinaryOperandError(Error):
    def __init__(self, first:str, second:str) -> None:
        super().__init__(f"Два бинарных оператора подряд: {first!r} и {second!r}")
class DivisionByZeroError(Error):
    def __init__(self) -> None:
        super().__init__("Деление на ноль")
class UnknownUnitError(Error):
    def __init__(self,unit:str) -> None:
        super().__init__(f"Неизвестная единица: {unit!r}")
class UncombinedUnitsError(Error):
    def __init__(self, first:str, second:str) -> None:
        super().__init__(f"Несовместимые единицы: {first!r} и {second!r}")
class BelowAbsoluteZeroValueError(Error):
    def __init__(self) -> None:
        super().__init__("Температура ниже абсолютного нуля")
