import mysql.connector
from mysql.connector import Error


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="170519",
    database="nik1"
)

mycursor = mydb.cursor()

# query for create table

# queryFirst="CREATE TABLE nikhil (id int, fullName varchar(255), email varchar(255));"

# query for set data in table

# queryFirst="INSERT INTO nikhil VALUES (109, 'harpreet', 'harpreet@gmail.com');"

# query for set data in table

# queryFirst="INSERT INTO nikhil VALUES (110, 'ishan', 'ishan@gmail.com');"

# query for create stored procedure

# queryFirst="""CREATE PROCEDURE nikhilwalaProcedure()
# BEGIN
# SELECT * FROM NIKHIL WHERE id = 110;
# END"""

# query for show stored procedure


queryFirst = "call nikhilWalaProcedure;"
try:
   mycursor.execute(queryFirst)
   myresult = mycursor.fetchall()
   for x in myresult:
    print(x)
   

except Error as e:
    print(f"error === {e}")
    mydb.rollback()

mydb.close()
