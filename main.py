import mysql.connector

username="root"
password="ExamplePassword"
host="localhost"
database="mydatabaseexample"

mydb = mysql.connector.connect(
  host=host,
  user=username,
  passwd=password
)


mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS " + database)

print("Database prepared")

mydb = mysql.connector.connect(
  host=host,
  user=username,
  passwd=password,
  database=database
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), address VARCHAR(255))")
print("tables prepared")


sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for row in myresult:
  print(row)



