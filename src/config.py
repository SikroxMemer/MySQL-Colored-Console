SQL_INFO = {"host" : "localhost" , "user" : "root" ,"password" : ""}

import mysql.connector

try:
    connection = mysql.connector.connect(**SQL_INFO)
except mysql.connector.Error as error:
    print(error)
    exit()
