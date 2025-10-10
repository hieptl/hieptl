#!/usr/bin/env python3
"""
Simple Python program for adding two numbers.
"""


def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b


def main():
    """Demonstrate number addition with examples."""
    print("Simple Number Addition Program")
    print("=" * 30)
    
    # Example additions
    examples = [
        (10, 20),
        (3.5, 2.7),
        (-5, 8),
        (0, 42),
        (100, -50)
    ]
    
    print("Example additions:")
    for a, b in examples:
        result = add_numbers(a, b)
        print(f"{a} + {b} = {result}")
    
    # Command line arguments
    import sys
    if len(sys.argv) == 3:
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
            result = add_numbers(num1, num2)
            print(f"\nCommand line result: {num1} + {num2} = {result}")
        except ValueError:
            print("\nError: Please provide two valid numbers as arguments.")
    elif len(sys.argv) > 1:
        print(f"\nUsage: python3 {sys.argv[0]} <number1> <number2>")


if __name__ == "__main__":
    main()