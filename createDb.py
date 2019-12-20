import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "@*data_rep",
    # database = "datarep",
    auth_plugin='mysql_native_password'
)

cursor - db.cursor()
cursor.execute("CREATE DATABASE datarepresentation")