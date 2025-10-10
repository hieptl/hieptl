#!/usr/bin/env python3
"""
A Python program for adding two numbers.
Demonstrates different approaches to number addition.
"""


def add_numbers(a, b):
    """
    Add two numbers and return the result.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
    
    Returns:
        The sum of a and b
    """
    return a + b


def get_number_input(prompt):
    """
    Get a number input from the user with error handling.
    
    Args:
        prompt: The prompt message to display
    
    Returns:
        A float number entered by the user
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    """Main function to run the addition program."""
    print("Python Number Addition Program")
    print("=" * 30)
    
    # Method 1: Interactive input
    print("\nMethod 1: Interactive Input")
    num1 = get_number_input("Enter the first number: ")
    num2 = get_number_input("Enter the second number: ")
    result = add_numbers(num1, num2)
    print(f"Result: {num1} + {num2} = {result}")
    
    # Method 2: Predefined values
    print("\nMethod 2: Predefined Values")
    examples = [
        (10, 20),
        (3.5, 2.7),
        (-5, 8),
        (0, 42)
    ]
    
    for a, b in examples:
        result = add_numbers(a, b)
        print(f"{a} + {b} = {result}")
    
    # Method 3: Command line arguments (if provided)
    import sys
    if len(sys.argv) == 3:
        try:
            arg1 = float(sys.argv[1])
            arg2 = float(sys.argv[2])
            result = add_numbers(arg1, arg2)
            print(f"\nCommand line: {arg1} + {arg2} = {result}")
        except ValueError:
            print("\nInvalid command line arguments. Please provide two numbers.")


if __name__ == "__main__":
    main()