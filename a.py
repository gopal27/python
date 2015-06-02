#!/usr/bin/python

import sys

def feb(n) :
  a, b = 0, 1
  while a < n:
    print a
    a, b = b, a+b

print sys.argv[1]
feb(sys.argv[1])
