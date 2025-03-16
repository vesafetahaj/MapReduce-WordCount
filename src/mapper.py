#!/usr/bin/env python3
import sys

# Read input from standard input
for line in sys.stdin:
    # Remove leading and trailing spaces
    line = line.strip()
    # Split the line into words
    words = line.split()
    # Output (word, 1) pair for each word
    for word in words:
        print(f"{word}\t1")
