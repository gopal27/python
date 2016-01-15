#!/usr/bin/python

from sys import argv

script, f1, f2 = argv

file1=open(f1, "r")
file2=open(f2, "r")


d = {}
for line in file1.readlines():
    arr = line.split(",")
    if len(arr[1]) > 0:
      d[arr[0]] = arr[1].strip()

for line in file2.readlines():
   a = line.split(",");
   if a[0] in d:
      print line.replace(a[0], d[a[0]], 1),
   else:
     print line,
