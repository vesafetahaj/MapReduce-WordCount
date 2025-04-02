from mapper import WordCountMapper
from reducer import WordCountReducer

def main():
    mapper = WordCountMapper()
    reducer = WordCountReducer()

    # Load input
    with open('../data/input.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Map phase
    mapped = []
    for line in lines:
        mapped.extend(mapper.map(line))

    # Optional: Write raw mapped output for inspection
    with open('../data/mapped_output.txt', 'w') as f:
        for word, count in mapped:
            f.write(f"{word}\t{count}\n")

    # Shuffle and sort phase
    grouped = reducer.shuffle_and_sort(mapped)

    # Reduce phase
    reduced = reducer.reduce(grouped)

    # Save the final output
    with open('../data/final_output2.txt', 'w') as f:
        for word in sorted(reduced):
            f.write(f"{word}: {reduced[word]}\n")

    print("MapReduce Word Count completed successfully!")

if __name__ == "__main__":
    main()
