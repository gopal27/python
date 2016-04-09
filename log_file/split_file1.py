#!/usr/bin/python

from sys import argv
script, f1, time = argv

file1=open(f1, "r")
time_arr = time.split(":")

for line in file1.readlines():
   log_time = line.split(" ")[0].split(":")
   if (log_time[0] >= time_arr[0] and
       log_time[1] >= time_arr[1] and
       log_time[2] >= time_arr[2]):
     print line,

  
