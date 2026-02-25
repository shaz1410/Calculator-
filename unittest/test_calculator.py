import unittest
from calculator import add, subtract, multiply, divide, power, modulus

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(5, 0), "Error: Cannot divide by zero!")

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(4, 2), 0)

if __name__ == "__main__":
    unittest.main()