class Error(Exception):
    pass
class EmptyExpressionError(Error):
    def __init__(self) -> None:
        super().__init__("Пустое выражение")

class InappropriateSymbolError(Error):
    def __init__(self) -> None:
        super().__init__("Недопустимый символ")
class InvalidNumberError(Error):
    def __init__(self, text: str) -> None:
        super().__init__(f"Некорректное число")

class MissedOperandError(Error):
    def __init__(self) -> None:
        super().__init__("Пропущенный операнд")

class DoubleBinaryOperandError(Error):
    def __init__(self, first: str, second: str) -> None:
        super().__init__(f"Два бинарных оператора подряд: {first!r} и {second!r}")
class DivisionByZeroError(Error):
    def __init__(self) -> None:
        super().__init__("Деление на ноль")
class UnknownUnitError(Error):
    def __init__(self) -> None:
        super().__init__("Неизвестная единица")
class UncombinedUnitsError(Error):
    def __init__(self) -> None:
        super().__init__("Несовместимые единицы")
class BelowAbsoluteZeroValueError(Error):
    def __init__(self) -> None:
        super().__init__("Температура ниже абсолютного нуля")
class UncombinedGroupConvertationError(Error):
    def __init__(self) -> None:
        super().__init__("Недопустимая конвертацяи величин")