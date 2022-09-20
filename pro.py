import mysql.connector as myconn
mydb = myconn.connect(
   host="localhost",
    user="root",
    password="170519",
    database="nik1"
)
obj = mydb.cursor()
# obj.callproc("myCustomer")
obj.callproc("SelectAllemployee")
for result in obj.stored_results():
    details = result.fetchall()

for det in details:  
    print(det)

obj.close()
mydb.close()