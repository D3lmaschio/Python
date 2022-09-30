import unittest
from modules import format


class FormatTestCase(unittest.TestCase):
    """Tests for 'format.py' module."""

    def test_format_location(self):
        """Test if return of format_location is neatly formatted."""
        result = format.format_location('brasil', 'são paulo')
        self.assertEqual(result, 'São Paulo, Brasil.')


if __name__ == '__main__':
    unittest.main()
