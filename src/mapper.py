class WordCountMapper:
    def map(self, line: str):
        # Splits the lines into words, converts them to lowercase, and emit (word, 1) for each
        return [(word.lower(), 1) for word in line.strip().split()]
