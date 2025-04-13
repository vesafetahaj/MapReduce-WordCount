from collections import defaultdict

class WordCountMapper:
    def map(self, line: str):
        # Splits the lines into words, converts them to lowercase, and emit (word, 1) for each
        return [(word.lower(), 1) for word in line.strip().split()]

    def combine(self, mapped_data):
        # Local reduction of mapped data to reduce intermediate results
        combined = defaultdict(int)
        for word, count in mapped_data:
            combined[word] += count
        return list(combined.items())  # Returns [(word, total)]
