#!/usr/bin/python


file1=open("file1.dat","r")
file2=open("file2.dat", "r")


d = {}
for line in file1.readlines():
    arr = line.split(",")
    d[arr[0]] = arr[1]

for line in file2.readlines():
   a = line.split(",");
   if a[0] in d:
      print line.replace(a[0], d[a[0]], 1)
   else:
     print line
