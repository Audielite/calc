import unittest
import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator.Calculator()

    def test_multiplication(self):
        result = self.calc.multiplication(4, 4)
        self.assertEqual(16, result)

    def test_multiplication_input_error(self):
        self.assertRaises(ValueError, self.calc.multiplication, "two", "three")

    def test_division(self):
        result = self.calc.division(4, 2)
        self.assertEqual(2, result)

    def test_division_input_error(self):
        self.assertRaises(ValueError, self.calc.division, "two", "three")

    def test_addition(self):
        result = self.calc.addition(3, 7)
        self.assertEqual(10, result)

    def test_addition_input_error(self):
        self.assertRaises(ValueError, self.calc.addition, "two", "three")

    def test_subtraction(self):
        result = self.calc.subtraction(8, 7)
        self.assertEqual(1, result)

    def test_subtraction_input_error(self):
        self.assertRaises(ValueError, self.calc.subtraction, "two", "three")


if __name__ == '__main__':
    unittest.main()