#!/usr/bin/python

import cx_Oracle

con = cx_Oracle.connect('hr/welcome@localhost:1521/xe')
ver = con.version.split('.')


print ver


for v in ver:
  if v == '11':
    print "It's 11"
  else:
    print "It's not 11"
 
con.close()
  
