#!/usr/bin/python3
import sys
import math

# Check for argument to avoid crash
if len(sys.argv) > 1:
    print(math.factorial(int(sys.argv[1])))
else:
    print("Usage: ./factorial.py <number>")
