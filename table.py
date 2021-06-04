import mysql.connector
from mysql.connector import Error


        
def create_table():
    
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database="jarvis",
                                             user='root',
                                             password='root',
                                             port=3307)
        if connection.is_connected():
            cursor = connection.cursor(buffered=True)
            cursor.execute("select database();")
            cursor.execute("show tables;")  
            record = cursor.fetchall()
            
            print("the number of tables is:",len(record))
            
            existed_tables=len(record)
            try:    
                cursor.execute("create table session{num}(input_command varchar(200));".\
                                   format(num=existed_tables+1))
                                               
            except Error as e:
                print("Error while connecting to MySQL", e)

            
            cursor.close()
            connection.commit()
            connection.close()
    except Error as e:
        print("Error while connecting to MySQL", e)

    return existed_tables+1