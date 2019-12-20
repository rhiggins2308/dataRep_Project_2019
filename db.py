import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "@*data_rep",
    database = "datarep"
)

cursor - db.cursor()

# INSERT
sql = "insert into student (name, age) values (%s, %s)"
values = ("Maire", 36)
cursor.execute(sql, values)
db.commit()

# SELECT
sql = "select * from student where id = %s"
values = (1,)
cursor.execute(sql, values)
result = cursor.fetchall()
# result = cursor.fetchOne()
for x in result:
    print(x)