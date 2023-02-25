import pyodbc

# conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=database.accdb;')
# cursor = conn.cursor()
# cursor.execute('select * from table_name')
   
# for row in cursor.fetchall():
#     print (row)

print(pyodbc.drivers())