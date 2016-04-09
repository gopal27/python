#!/usr/bin/python

from sys import argv
script, f1, time = argv

f=open(f1,'r')
time_arr = time.split(':')

for l in f.readlines():
   arr = l.split(' ')[0].split(':')
   if (arr[0] > time_arr[0] or
       (arr[0] == time_arr[0] and arr[1] > time_arr[1]) or
       (arr[0] == time_arr[0] and arr[1] == time_arr[1] and arr[2] >= time_arr[2])):
       print l,


