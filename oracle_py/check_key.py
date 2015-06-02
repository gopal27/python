#!/usr/bin/python

from sys import argv
from sets import Set

script, f1, f2 = argv

s1 = Set()
lines=open(f1).readlines()
for line in lines:
  s1.add(line.split(',')[0])

s2 = Set()
lines=open(f2).readlines()
for line in lines:
  s2.add(line.split(',')[0])


#checking the difference
s3 = s1 - s2
print "missing keys..."
for x in s3:
  print x
