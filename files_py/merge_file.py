#!/usr/bin/python

from sets import Set

file1=open("file1.dat","r")
file2=open("file2.dat", "r")

foutput = open("file_merged.dat", "w")

s1 = Set()
for line in file1.readlines():
    s1.add(line.split(",")[0])
    foutput.write(line)


for line in file2.readlines():
   if line.split(",")[0] not in s1:
       s1.add(line.split(",")[0])
       foutput.write(line)

  
    
  
