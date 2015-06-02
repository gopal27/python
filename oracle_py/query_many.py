#!/usr/bin/python

import cx_Oracle

con = cx_Oracle.connect("hr/welcome@localhost:1521/xe")
cur = con.cursor()

cur.execute("select * from departments order by department_id")

row = cur.fetchmany(3)
print row

row = cur.fetchmany(numRows=2)
print row

#TypeError: 'rows' is an invalid keyword argument for this function
#row = cur.fetchmany(rows=4)
print row

cur.close()
con.close()
