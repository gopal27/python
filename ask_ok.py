#!/usr/bin/python


def ask_ok(prompt, noOfTries = 2, complaint="Yes or no, please!"):
  "method def - ask_ok"
  while True:
    ok = raw_input(prompt)
    if ok in ('y', 'ye', 'yes'):
      return True
    if ok in ('n','no', 'nop', 'nope'):
      return False

    noOfTries = noOfTries - 1
    if noOfTries < 0:
      raise IOError("Invalid user input!")
   
    print complaint


print ask_ok('Do you want to quit?')
    
    
