#!/usr/bin/python3

def islower(c):
    return ord('a') <= ord(c) <= ord('z')

# Testing the function
print("a is", "lower" if islower("a") else "upper")
print("H is", "lower" if islower("H") else "upper")
