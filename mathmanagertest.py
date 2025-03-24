import unittest
from calculator import calculate_income_tax, calculate_monthly_interest, degree_classification

class TestCalculator(unittest.TestCase):
    def test_income_tax(self):
        self.assertEqual(calculate_income_tax(12500), 0)
        self.assertEqual(calculate_income_tax(30000), 3486)
        self.assertEqual(calculate_income_tax(60000), 8720)

    def test_monthly_interest(self):
        self.assertAlmostEqual(calculate_monthly_interest(1000, 1), 3.1667, places=4)
        self.assertAlmostEqual(calculate_monthly_interest(1000, 2), 3.0000, places=4)

    def test_degree_classification(self):
        self.assertEqual(degree_classification([70, 60, 50, 40], [20, 20, 20, 20]), "Upper Second Class")
        self.assertEqual(degree_classification([90, 85, 80, 78], [30, 30, 20, 20]), "First Class")

if __name__ == '__main__':
    unittest.main()

