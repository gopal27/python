#!/usr/bin/python

def do_twice(f):
  f()
  f()

def print_spam():
  print "Spam..."


do_twice(print_spam)
