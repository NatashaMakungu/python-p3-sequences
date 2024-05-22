#!/usr/bin/env python3

def print_fibonacci(length):
    """Prints the Fibonacci sequence up to the given length."""
    if length <= 0:
        print([])
        return

    sequence = [0, 1]
    while len(sequence) < length:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    print(sequence[:length])

# Example:
print_fibonacci(9)