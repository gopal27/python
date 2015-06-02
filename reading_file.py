#!/usr/bin/python

# Reading a file & prints them with line no

import sys

#open the file
fin = open(sys.argv[1], 'r')

#print the contents
lno = 1
while 1:
  line = fin.readline()
  if not line: break
  
  print '%5d: %-s' % (lno, line[:-1])
  lno = lno + 1
 
fin.close

