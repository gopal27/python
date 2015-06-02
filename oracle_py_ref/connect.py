import cx_Oracle

#con = cx_Oracle.connect('pythonhol/welcome@localhost/orcl') 
con = cx_Oracle.connect('hr/welcome@localhost/xe') 
print con.version

con.close()
