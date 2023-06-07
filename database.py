import mysql.connector
database = mysql.connector.connect(
    host = 'localhost',
    user = 'mysql',
    passwd = '12345'
)

cursor_object = database.cursor()

cursor_object.execute("CREATE DATABASE dcrm_db")

print('ALL DONE!')