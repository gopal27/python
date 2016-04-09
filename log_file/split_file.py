#!/usr/bin/python

from sys import argv
script, f1, time = argv

file1=open(f1, "r")
input_time = time.split(":");
for line in file1.readlines():
    time = line.split(" ")[0]
    time_arr = time.split(":")
    if(time_arr[0] >= input_time[0] and
       time_arr[1] >= input_time[1] and
       time_arr[2] >= input_time[2]):
       print line, 
