#!/usr/bin/python

from sys import argv

script = argv

def check_leap_year(year):
  if year % 4 == 0:
      if year % 100 != 0 or year % 400 == 0:
          return True
   
  return False


while True:
  y=input("What year:")

  isLeap = check_leap_year(y)

  if isLeap:
    print y, " is a leap year."
  else:
    print y, " is not a leap year."


 
