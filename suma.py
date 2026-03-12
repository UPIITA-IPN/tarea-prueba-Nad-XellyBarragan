#!/usr/bin/env python3
import sys
if len(sys.argv) != 3:
    print("Usage: python suma.py <num1> <num2>", file=sys.stderr)
    sys.exit(1)
try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(a + b)
except ValueError:
    print("Error: Arguments must be integers", file=sys.stderr)
    sys.exit(1)
