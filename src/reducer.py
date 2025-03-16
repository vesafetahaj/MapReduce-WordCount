#!/usr/bin/env python3
import sys

current_word = None
current_count = 0
word = None

# Read input from standard input
for line in sys.stdin:
    line = line.strip()
    word, count = line.split("\t", 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

# Print the last word count
if current_word == word:
    print(f"{current_word}\t{current_count}")
