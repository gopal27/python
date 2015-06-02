#!/usr/bin/python

from sys import argv
import getopt


print "NOTE:: Need to always pass [1:]....excluding the script name at [0] \n"
opts, args = getopt.getopt(argv[1:], 'a:b:c:')
print "opts ", type(opts), " = ", opts
print "args ", type(args), " =", args

cmdMap = dict(opts)

print cmdMap

print "-a value is:", cmdMap['-a']
print "-b value is:", cmdMap['-b']
print "-c value is:", cmdMap['-c']
