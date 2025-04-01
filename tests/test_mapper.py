import unittest
from src.mapper import WordCountMapper

class TestWordCountMapper(unittest.TestCase):

    def setUp(self):
        self.mapper = WordCountMapper()

    def test_single_line(self):
        line = "Hello world"
        expected = [('hello', 1), ('world', 1)]
        self.assertEqual(self.mapper.map(line), expected)

    def test_case_insensitivity(self):
        line = "Hello hello"
        expected = [('hello', 1), ('hello', 1)]
        self.assertEqual(self.mapper.map(line), expected)

    def test_strip_and_split(self):
        line = "  Hello   world  "
        expected = [('hello', 1), ('world', 1)]
        self.assertEqual(self.mapper.map(line), expected)

if __name__ == '__main__':
    unittest.main()
