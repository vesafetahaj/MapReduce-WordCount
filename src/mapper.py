#!/usr/bin/env python3
import sys
import string

# Read input from standard input
for line in sys.stdin:
    # Remove leading and trailing spaces
    line = line.strip()
    # Remove punctuation
    line = line.translate(str.maketrans('', '', string.punctuation))
    # Split the line into words
    words = line.split()
    # Output (word, 1) pair for each word
    for word in words:
        print(f"{word.lower()}\t1")  # Convert to lowercase for consistency
