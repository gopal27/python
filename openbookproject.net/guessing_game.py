#!/usr/bin/python

import random


def check(guess, inp, count):
  if guess == inp:
    print "Congratulations...it took %d guess", count,
  elif inp > guess:
    print "Too high. try againp!",
    inp=input();
    count = count + 1
    check(guess, inp, count)
  elif inp < guess:
    print "Too low.  try againp!",
    inp=input()
    count = count + 1
    check(guess, inp, count)

   
while True:
  print "Time to play a guessing game!",
  guess = random.randint(1, 100);
  inp = input("Entere a number betweeen 1 to 100:");
  check(guess, inp, 1);
