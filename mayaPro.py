import mysql.connector 
from mysql.connector import Error


mydb = mysql.connector.connect(
   host="localhost",
    user="root",
    password="170519",
    database="nik1"
)

mycursor = mydb.cursor()
queryFirst="call mayaWalaProcedure;"


# mycursor.execute(queryFirst)
try:
   mycursor.execute(queryFirst)
   myresult = mycursor.fetchall()
   for x in myresult:
    print(x)
   

except Error as e:
    print(f"error === {e}")
    mydb.rollback()

mydb.close()
# mycursor.execute("CREATE PROCEDURE showAllCustomers AS SELECT * FROM customer;")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)