import unittest
from simple_calculator import SimpleCalculator


    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(1.2, 2.5, 3.7))
        self.assertEqual(self.calc.add(0, 0, 0))

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.add(1, 1), 0)
        self.assertEqual(self.calc.add(-2, -3), 1)
        self.assertEqual(self.calc.add(2.5, 1.2, 1.3))
        self.assertEqual(self.calc.add(0, 0, 0))
        self.assertEqual(self.calc.add(-3, -5), 1)
    def test_multiplication(self):
        """Test multiplication with ints, negatives, zero and floats."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(2.5, 1.2), 3.0)
     def test_division_normal(self):
        """Test normal division results (returns float)."""
        self.assertEqual(self.calc.divide(10, 5), 2.0)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(-6, 3), -2.0)
        self.assertEqual(self.calc.divide(1, 3), 1/3)
    def test_division_by_zero(self):
         """Division by zero should return None according to implementation."""
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

if __name__ == "__main__":
    unittest.main()
