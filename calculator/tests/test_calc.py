from decimal import DivisionByZero
import pytest
from calculator import calc

def test_add():
  assert calc.add(2, 2) == 2 + 2

def test_add_nan():
  with pytest.raises(ValueError):
    calc.add(2, 'b')

def test_add_two_nan():
  with pytest.raises(ValueError):
    calc.add('a', 'b')

def test_subtract():
  assert calc.subtract(2, 2) == 2 - 2

def test_subtract_nan():
  with pytest.raises(ValueError):
    calc.subtract(2, 'b')

def test_subtract_two_nan():
  with pytest.raises(ValueError):
    calc.subtract('a', 'b')

def test_multiply():
  assert calc.multiply(2, 2) == 2 * 2

def test_multiply_nan():
  with pytest.raises(ValueError):
    calc.multiply(2, 'a')

def test_multiply_two_nan():
  with pytest.raises(ValueError):
    calc.multiply('b', 'a')

def test_divide():
  assert calc.divide(2, 2) == 2 / 2

def test_divide_nan():
  with pytest.raises(ValueError):
    calc.divide(2, 'b')

def test_divide_two_nan():
  with pytest.raises(ValueError):
    calc.divide('a', 'b')

def test_divide_by_zero():
  with pytest.raises(ZeroDivisionError):
    calc.divide(2, 0)

