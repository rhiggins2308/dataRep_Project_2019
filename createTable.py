import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "@M4ir3s_2308@",
    database = "rugby"
)

cursor = db.cursor()
# sql = "CREATE TABLE league (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100))"
sql = "CREATE TABLE team (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), conf VARCHAR(10), country VARCHAR(100), points INT)" 
cursor.execute(sql)