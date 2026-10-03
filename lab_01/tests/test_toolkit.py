import pytest

from toolkit.__main__ import main
from toolkit.calculator import calculate
from toolkit.errors import (
    DivisionByZeroError,
    DoubleBinaryOperandError,
    EmptyExpressionError,
    InappropriateSymbolError,
    InvalidNumberError,
    MissedOperandError,
)


# Положительные тесты
def test_pos1() -> None:
    assert calculate('1 + 1') == 2.0

def test_pos2() -> None:
    assert calculate('1 + 2 * 3') == 7.0

def test_pos3() -> None:
    assert calculate('1 - 2 - 3') == -4.0

def test_pos4() -> None:
    assert calculate('1 * -2') == -2.0
    assert calculate('-1 + 2') == 1

def test_5() -> None:
    assert calculate('0.5 * 2') == 1.0

# Негативные тесты
def test_neg1() -> None:
    with pytest.raises(EmptyExpressionError):
        calculate('')

def test_neg2() -> None:
    with pytest.raises(MissedOperandError):
        calculate('1 +')

def test_neg3() -> None:
    with pytest.raises(DoubleBinaryOperandError):
        calculate('1 + * 2')

def test_neg4() -> None:
    with pytest.raises(InappropriateSymbolError):
        calculate('1 + a')

def test_neg5() -> None:
    with pytest.raises(InvalidNumberError):
        calculate('1.2.3')

def test_neg6() -> None:
    with pytest.raises(DivisionByZeroError):
        calculate('1 / 0')

# Тесты CLI
def test_cli1(capsys: pytest.CaptureFixture[str]) -> None:
    code = main(["calc", "2+2"])
    out, err = capsys.readouterr()
    assert code == 0
    assert out.strip() == "4.0"
    assert err == ""

def test_cli2(capsys: pytest.CaptureFixture[str]) -> None:
    code = main(["calc", "2 +"])
    out, err = capsys.readouterr()
    assert code == 2
    assert out == ""
    assert "error" in err