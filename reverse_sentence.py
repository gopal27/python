#!/usr/bin/python

from sys import argv

script = argv

#DEBUG = True
DEBUG = False

def reverse_sentence(sentence):
    words = ()
    if sentence is not None:
      words = sentence.split(" ")
    else:
      return None

    #reverse the array
    rightIndex = len(words) - 1
 
    if DEBUG:
      print "rightIndex:",rightIndex
      print "range(0,len(words))",range(0,len(words))
    for i in range(0, len(words)):
      if i >= rightIndex: break
      else:
	 temp = words[i]
	 words[i] = words[rightIndex]
	 words[rightIndex] = temp
	 i = i + 1
	 rightIndex = rightIndex - 1

    return words


while True:
  sen=raw_input("Enter a sentence to reverse: ")
  
  if DEBUG:
    print "Entered: ", sen

  result = reverse_sentence(sen)
  
  output_str = ""
  for i in result:
    if output_str != "":
        output_str = output_str + " "
    output_str = output_str + i
    
  print "Reversed sentence: ", output_str


  
   
  
