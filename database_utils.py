import pyodbc


def get_connection():
    return pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=./database.accdb;')


def get_tables():
    cursor = get_connection().cursor()
    return [table.table_name for table in cursor.tables(tableType='Table')]


def get_columns(table_name):
    cursor = get_connection().cursor()
    res = cursor.execute(f"SELECT * FROM {table_name} WHERE 1=0".format(table_name))
    return [tuple[0] for tuple in res.description]
