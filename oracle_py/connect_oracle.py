#!/usr/bin/python


import cx_Oracle

con = cx_Oracle.connect("hr/welcome@localhost:1521/xe")
print con.version

print con.version.split('.')

con.close()
