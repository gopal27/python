#!/usr/bin/python


import cx_Oracle

con = cx_Oracle.connect("hr/welcome@localhost:1521/xe")
cur = con.cursor()

cur.execute("Select * from departments order by department_id")

for r in cur:
  print r

cur.close()
con.close()
