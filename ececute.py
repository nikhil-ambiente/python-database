import mysql.connector 
from mysql.connector import Error


mydb = mysql.connector.connect(
   host="localhost",
    user="root",
    password="170519",
    database="nik1"
)

mycursor = mydb.cursor()
queryFirst="CREATE TABLE nikhil (id int, fullName varchar(255), email varchar(255));"
# queryFirst="INSERT INTO mayank VALUES (111, 'manan', 'manan@gmail.com');"
try:
   mycursor.execute(queryFirst)
#    myresult = mycursor.fetchall()
#    for x in myresult:
    # print(x)
   mydb.commit()
   

except Error as e:
    print(f"error === {e}")
    mydb.rollback()

mydb.close()
# mycursor.execute("CREATE PROCEDURE showAllCustomers AS SELECT * FROM customer;")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)