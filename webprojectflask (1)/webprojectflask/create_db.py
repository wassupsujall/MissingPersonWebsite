import mysql.connector
mydb = mysql.connector.connect(
    host="server",
    user="root",
    passwd="12345678"
    )

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE our_user")

my_cursor.execute("SHOW DATABASES")
for mydb in my_cursor:
    print(mydb)