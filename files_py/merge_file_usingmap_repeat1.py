#!/usr/bin/python


cmdmap = dict(f1='file1.dat', f2='file2.dat')

file1 = open(cmdmap['f1'], 'r')
file2 = open(cmdmap['f2'], 'r')

foutput = open('output.dat', 'w')

m1 = {}
for line in file1.readlines():
    m1[int(line.split(',')[0])] = line

m2 = {}
for line in file2.readlines():
    m2[int(line.split(',')[0])] = line

s1 = set(m1.keys())
s2 = set(m2.keys())

s3 = sorted(s1 | s2)

for key in s3:
  if key in s1:
    foutput.write(m1[key])
  if key in s2:
    foutput.write(m2[key])

foutput.close()
file1.close()
file2.close()

f = open('output.dat','r')
for l in f.readlines():
    print l

