from decimal import DivisionByZero
import pytest
from calculator import calc

def test_add():
  assert calc.add(2, 2) == 2 + 2

def test_add_nan():
  with pytest.raises(TypeError):
    calc.add(2, '2')

def test_add_two_nan():
  with pytest.raises(ValueError):
    calc.add('2', '2')

def test_subtract():
  assert calc.subtract(2, 2) == 2 - 2

def test_subtract_nan():
  with pytest.raises(TypeError):
    calc.add(2, '2')

def test_subtract_two_nan():
  with pytest.raises(ValueError):
    calc.add('2', '2')

def test_multiply():
  assert calc.multiply(2, 2) == 2 * 2

def test_multiply_nan():
  with pytest.raises(TypeError):
    calc.add(2, '2')

def test_multiply_two_nan():
  with pytest.raises(ValueError):
    calc.add('2', '2')

def test_divide():
  assert calc.divide(2, 2) == 2 / 2

def test_divide_nan():
  with pytest.raises(TypeError):
    calc.add(2, '2')

def test_divide_two_nan():
  with pytest.raises(ValueError):
    calc.add('2', '2')

def test_divide_by_zero():
  with pytest.raises(ZeroDivisionError):
    calc.divide(2, 0)

