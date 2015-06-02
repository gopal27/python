#!/usr/bin/python


import cx_Oracle

con = cx_Oracle.connect('hr/welcome@localhost:1521/xe')
ver = con.version.split('.')

print ver
print ver.index("0")

ver.remove("2")
print ver


ver1 = ["11", "g"]
ver2 = ["R", "2"]
print ver1 + ver2

con.close()

