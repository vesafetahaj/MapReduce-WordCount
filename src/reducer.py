from collections import defaultdict

class WordCountReducer:
    def shuffle_and_sort(self, mapped_data):
        grouped = defaultdict(list)
        for word, count in mapped_data:
            grouped[word].append(count)
        return grouped

    def reduce(self, grouped_data):
        return {word: sum(counts) for word, counts in grouped_data.items()}
