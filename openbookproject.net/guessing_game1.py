#!/usr/bin/python

import random;

def check_guess(guess, inp, count):
  if guess == inp:
     print "Congratulations... It took %d tries to find the guess",count
  elif guess > inp:
     print("Too low...try again");
     inp = input()
     check_guess(guess, inp, count + 1)
  elif guess < inp:
     print("Too high...try again");
     inp = input()
     check_guess(guess, inp, count + 1)


while True:
  print "Let's start the guessing game..."
  guess = random.randint(1,100)
  inp = input("Enter a number betwee 1 to 100: ")
  check_guess(guess, inp, 1)
