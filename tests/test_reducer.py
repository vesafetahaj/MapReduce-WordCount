import unittest
from src.reducer import WordCountReducer

class TestWordCountReducer(unittest.TestCase):

    def setUp(self):
        self.reducer = WordCountReducer()

    def test_shuffle_and_sort(self):
        mapped = [('hello', 1), ('world', 1), ('hello', 1)]
        grouped = self.reducer.shuffle_and_sort(mapped)
        self.assertEqual(grouped['hello'], [1, 1])
        self.assertEqual(grouped['world'], [1])

    def test_reduce(self):
        grouped = {'hello': [1, 1], 'world': [1]}
        reduced = self.reducer.reduce(grouped)
        self.assertEqual(reduced, {'hello': 2, 'world': 1})

if __name__ == '__main__':
    unittest.main()
