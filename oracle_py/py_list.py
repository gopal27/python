#!/usr/bin/python

import cx_Oracle

con = cx_Oracle.connect('hr/welcome@localhost:1521/xe')
ver = con.version.split('.')


#print the list
print ver
print ver[0]
print ver[-1]
print ver[1:4]

con.close()
