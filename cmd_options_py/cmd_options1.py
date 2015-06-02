#!/usr/bin/python

from sys import argv
import getopt

opts, args = getopt.getopt(argv[1:], 'a:b:c:')
cmdMap = dict(opts)

print cmdMap

