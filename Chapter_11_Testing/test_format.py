import unittest
from modules import format


class FormatTestCase(unittest.TestCase):
    """Tests for 'format.py' module."""

    def test_format_location(self):
        """Test if return of format_location is neatly formatted."""
        result = format.format_location('brasil', 'são paulo', '12.330.000')
        self.assertEqual(result, 'São Paulo, Brasil - Population: 12.330.000')


if __name__ == '__main__':
    unittest.main()
