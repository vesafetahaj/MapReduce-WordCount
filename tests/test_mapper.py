import unittest
from src.mapper import WordCountMapper

class TestWordCountMapper(unittest.TestCase):
    def setUp(self):
        self.mapper = WordCountMapper()

    def test_single_line_mapping(self):
        """Test mapping a basic sentence."""
        line = "Hello world"
        expected = [('hello', 1), ('world', 1)]
        result = self.mapper.map(line)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_case_insensitivity(self):
        """Test that words are converted to lowercase."""
        line = "Hello hello"
        expected = [('hello', 1), ('hello', 1)]
        result = self.mapper.map(line)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

    def test_strip_and_split(self):
        """Test that extra spaces are handled correctly."""
        line = "  Hello   world  "
        expected = [('hello', 1), ('world', 1)]
        result = self.mapper.map(line)
        self.assertEqual(result, expected, f"Expected {expected}, but got {result}")

if __name__ == '__main__':
    unittest.main(verbosity=2)
