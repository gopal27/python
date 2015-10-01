#!/usr/bin/python

def compress(inputStr):
    # Compressing a string 
    count = 1
    lastChar = inputStr[0]
    result = "" 
    for i in range(1, len(inputStr)):
        if lastChar == inputStr[i]:
            count = count + 1
        else:
           result = result + lastChar
           result = result + str(count)
           count = 1
           lastChar = inputStr[i]

    result = result + lastChar
    result = result + str(count)
    if len(inputStr) <= len(result):
       return inputStr
    else:
       return result


testInput = "aaabbbcccccddddddi"
print testInput, compress(testInput)


#print compress("")

testInput = "aa"
print testInput, compress(testInput)

   
