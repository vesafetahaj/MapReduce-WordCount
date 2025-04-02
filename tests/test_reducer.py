import unittest
from src.reducer import WordCountReducer

class TestWordCountReducer(unittest.TestCase):
    def setUp(self):
        self.reducer = WordCountReducer()

    def test_shuffle_and_sort_grouping(self):
        """Test that words are correctly grouped after shuffle/sort."""
        mapped = [('hello', 1), ('world', 1), ('hello', 1)]
        grouped = self.reducer.shuffle_and_sort(mapped)
        self.assertEqual(grouped['hello'], [1, 1], f"Expected [1, 1] for 'hello', got {grouped['hello']}")
        self.assertEqual(grouped['world'], [1], f"Expected [1] for 'world', got {grouped['world']}")

    def test_reduce_summing(self):
        """Test summing of grouped counts."""
        grouped = {'hello': [1, 1], 'world': [1]}
        reduced = self.reducer.reduce(grouped)
        expected = {'hello': 2, 'world': 1}
        self.assertEqual(reduced, expected, f"Expected {expected}, but got {reduced}")

if __name__ == '__main__':
    unittest.main(verbosity=2)
