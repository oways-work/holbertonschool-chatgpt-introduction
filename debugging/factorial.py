#!/usr/bin/python3
import sys
import math

if len(sys.argv) > 1:
    print(math.factorial(int(sys.argv[1])))
else:
    print("Error: You must provide a number.")
    print("Usage: ./factorial.py <number>")
