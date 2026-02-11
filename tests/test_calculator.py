import calculator


def test_add():
    assert calculator.add(2, 3) == 5


def test_subtract():
    assert calculator.subtract(10, 5) == 5


def test_multiply():
    assert calculator.multiply(4, 5) == 20


def test_divide():
    assert calculator.divide(10, 2) == 5


def test_divide_by_zero():
    assert calculator.divide(10, 0) == "Error: Cannot divide by zero!"


def test_power():
    assert calculator.power(2, 3) == 8


def test_modulus():
    assert calculator.modulus(10, 3) == 1
