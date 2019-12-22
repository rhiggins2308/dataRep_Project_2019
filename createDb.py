import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "@M4ir3s_2308@",
    # database = "datarepresentation"
)

cursor = db.cursor()
sql = "CREATE DATABASE rugby"
cursor.execute(sql)