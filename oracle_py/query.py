#!/usr/bin/python

# Python Quering Oracle db.

import cx_Oracle

# create con & cur
con = cx_Oracle.connect("hr/welcome@localhost:1521/xe")
cur = con.cursor()

# parse query & execute via cursor
cur.execute("select * from departments order by department_id")

# retrieve the results
for result in cur:
  print result


# Close the cursor & connection
cur.close()
con.close()



