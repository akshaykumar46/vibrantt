import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='root',
                                         port=3307)
    print(connection)
    print("successfully connected")
    

except Error as e:
    print("Error while connecting to MySQL", e)
