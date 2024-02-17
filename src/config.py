SQL_INFO = {"host" : "localhost" , "user" : "root" ,"password" : "789456123Simo11"}



import mysql.connector

try:
    connection = mysql.connector.connect(**SQL_INFO)

except mysql.connector.Error as error:
    print(error)
    exit()
