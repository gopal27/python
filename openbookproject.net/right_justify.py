#!/usr/bin/python

from sys import argv

script, s = argv

def right_justify(s):
  l = len(s)
  spaces = 70 - l
  i = 1
  while i < spaces: 
     print " ",
     i = i + 1;
  print s

right_justify(s)
