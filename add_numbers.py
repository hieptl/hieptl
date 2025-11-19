#!/usr/bin/env python3
"""
A simple Python program for adding two numbers.
Supports both command-line arguments and interactive input.
"""

import sys


def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b


def get_number_input(prompt):
    """Get a number from user input with error handling."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    """Main function to handle different input methods."""
    if len(sys.argv) == 3:
        # Command-line arguments provided
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
        except ValueError:
            print("Error: Please provide valid numbers as arguments.")
            print("Usage: python add_numbers.py <number1> <number2>")
            sys.exit(1)
    else:
        # Interactive input
        print("Welcome to the Number Addition Program!")
        num1 = get_number_input("Enter the first number: ")
        num2 = get_number_input("Enter the second number: ")
    
    result = add_numbers(num1, num2)
    print(f"{num1} + {num2} = {result}")


if __name__ == "__main__":
    main()