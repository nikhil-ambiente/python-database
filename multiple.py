import mysql.connector
from mysql.connector import Error


meriList = []
mydbmiks = mysql.connector.connect(
    host="localhost",
    user="root",
    password="170519",
    database="miks"
)
mydbniks = mysql.connector.connect(
    host="localhost",
    user="root",
    password="170519",
    database="nik1"
)
mydbviks = mysql.connector.connect(
    host="localhost",
    user="root",
    password="170519",
    database="viks"
)
mydbnikss = mysql.connector.connect(
    host="localhost",
    user="root",
    password="170519",
    database="nik2"
)

# meriList.append(mydbmiks)
# meriList.append(mydbniks)
# meriList.append(mydbviks)

print("localhost")


mycursor1 = mydbmiks
print(mycursor1)
mycursor2 = mydbniks
mycursor3 = mydbviks
mycursor4 = mydbnikss

meriList.append(mycursor1)
meriList.append(mycursor2)
meriList.append(mycursor3)
meriList.append(mycursor4)

print(meriList)
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

queryFirst="""DROP PROCEDURE IF EXISTS mikssWalaProcedure; 
CREATE PROCEDURE mikssWalaProcedure()
BEGIN
CREATE TABLE nikhil (id int, fullName varchar(255), email varchar(255));
END"""

# query for show stored procedure


# queryFirst = "call nikhilWalaProcedure;"
try:
    for i in meriList[1:]:
        i.cursor().execute(queryFirst)
        mydbmiks.close()
        
        
#    mycursor.execute(queryFirst)
#    myresult = mycursor.fetchall()
#    for x in myresult:
#     print(x)
   

except Error as e:
    print(f"error === {e}")
    mydbmiks.rollback()

# mydbmiks.close()
