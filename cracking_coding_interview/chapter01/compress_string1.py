#!/usr/bin/python


def compress(inputString) :
    """ Compression of input String """

    count = 1
    lastChar = inputString[0]
    result = ""
    for i in range(1, len(inputString)):
       if lastChar == inputString[i]:
           count += 1
       else:
           result += lastChar
           result += str(count)
           lastChar = inputString[i]
           count = 1
    result += lastChar
    result += str(count)

 
    if len(inputString) <= len(result):
        return inputString
    else:
        return result



test_input = "aaabbbcccddeffggggg"
print test_input, compress(test_input)

test_input = "yyyy333"
print test_input, compress(test_input)

 
  
