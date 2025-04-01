class WordCountMapper:
    def map(self, line: str):
        return [(word.lower(), 1) for word in line.strip().split()]
