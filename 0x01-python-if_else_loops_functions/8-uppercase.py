#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - 32)  # Convert to uppercase
        print(char, end="")
    print()

# Testing the function
uppercase("best")
uppercase("Best School 98 Battery street")
