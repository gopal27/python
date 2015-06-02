#!/usr/bin/python

#Connecting using the DRCP - Database Resident Connection Pooling

import cx_Oracle

# pooled connection
con = cx_Oracle.connect("hr", "welcome", "localhost:1521/xe:pooled",cclass="hr",purity=cx_Oracle.ATTR_PURITY_SELF)
print con.version

con.close()
