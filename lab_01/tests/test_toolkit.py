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
def test_pos1():
    assert calculate('1 + 1') == 2.0

def test_pos2():
    assert calculate('1 + 2 * 3') == 7.0

def test_pos3():
    assert calculate('1 - 2 - 3') == -4.0

def test_pos4():
    assert calculate('1 * -2') == -2.0
    assert calculate('-1 + 2') == 1

def test_5():
    assert calculate('0.5 * 2') == 1.0

# Негативные тесты
def test_neg1():
    with pytest.raises(EmptyExpressionError):
        calculate('')

def test_neg2():
    with pytest.raises(MissedOperandError):
        calculate('1 +')

def test_neg3():
    with pytest.raises(DoubleBinaryOperandError):
        calculate('1 + * 2')

def test_neg4():
    with pytest.raises(InappropriateSymbolError):
        calculate('1 + a')

def test_neg5():
    with pytest.raises(InvalidNumberError):
        calculate('1.2.3')

def test_neg6():
    with pytest.raises(DivisionByZeroError):
        calculate('1 / 0')

# Тесты CLI
def test_cli1(capsys):
    code = main(["calc", "2+2"])
    out, err = capsys.readouterr()
    assert code == 0
    assert out.strip() == "4.0"
    assert err == ""

def test_cli2(capsys):
    code = main(["calc", "2 +"])
    out, err = capsys.readouterr()
    assert code == 2
    assert out == ""
    assert "error" in err