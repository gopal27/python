#!/usr/bin/python

from sys import argv
import getopt

#opts, args = getopt.getopt(argv[1:], 'x', ['f1=', 'f2='])
cmdmap = dict(f1='file1.dat',f2='file2.dat')

#print cmdmap
file1 = open(cmdmap['f1'], 'r')
file2 = open(cmdmap['f2'], 'r')

map1 = {}
for line in file1.readlines():
  map1[int(line.split(",")[0])] = line

map2 = {}
for line in file2.readlines():
  map2[int(line.split(",")[0])] = line

s1 = set(map1.keys())
s2 = set(map2.keys())

s3 = sorted(s1 | s2)

print "Sorted unique keys..."
print s3


for key in s3:
  if key in map1:
     print map1[key]
  elif key in map2:
     print map2[key]



