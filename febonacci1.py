#!/usr/bin/python

#Python programming

import sys

def feb(n):
  a, b = 0, 1
  while a < n :
    print(a)
    a, b = b, a+b
 
#feb(sys.argv[1])

print sys.argv[1]
feb(10) 
