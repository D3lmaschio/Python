import unittest
from modules.employee import Employee


class TestEmployee(unittest.TestCase):
    """Test for Employee Class"""

    def setUp(self):
        """Create a Employee with default attr to test all methods."""
        self.employee = Employee('Matheus', 'Delmaschio', 100_000)

    def test_give_default_raise(self):
        """Test with default raise (default=5000)."""
        self.employee.give_raise()
        self.assertEqual(105_000, self.employee.annual_salary)

    def test_give_custom_raise(self):
        """Test with a custom raise(10_000)."""
        self.employee.give_raise(10_000)
        self.assertEqual(110_000, self.employee.annual_salary)
