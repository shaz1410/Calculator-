import tests
from GUI import evaluate_expression

class TestGUIFunctions(tests.TestCase):

    def test_addition(self):
        self.assertEqual(evaluate_expression("2+3"), 5)

    def test_subtraction(self):
        self.assertEqual(evaluate_expression("10-4"), 6)

    def test_multiplication(self):
        self.assertEqual(evaluate_expression("5*6"), 30)

    def test_division(self):
        self.assertEqual(evaluate_expression("8/2"), 4)
        self.assertEqual(evaluate_expression("5/0"), "Error: Cannot divide by zero!")

    def test_power(self):
        self.assertEqual(evaluate_expression("2**3"), 8)

    def test_modulus(self):
        self.assertEqual(evaluate_expression("10%3"), 1)

    def test_invalid_input(self):
        self.assertEqual(evaluate_expression("abc+1"), "Error: Invalid input!")
        self.assertEqual(evaluate_expression("2++3"), "Error: Invalid input!")

if __name__ == "__main__":
    tests.main()
