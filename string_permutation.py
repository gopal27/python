#!/usr/bin/python

from sys import argv

script, input = argv

def print_all_permutations(input):
    # Prints all permutations of the input string

    if len(input) == 0:
        return
    elif len(input) == 1:
        print(input)
        return
    else:
        permUtil("", input)


def permUtil(part1, remaining):
   if len(remaining) == 0:
      print part1 
   else:
      for i in range(0, len(remaining)):
         permUtil(part1 + remaining[i], remaining[:i] + remaining[i+1:])
  

print_all_permutations(input)
