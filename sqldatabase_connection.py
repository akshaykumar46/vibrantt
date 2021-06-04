import mysql.connector
import tkinter
import tkinter.messagebox
from mysql.connector import Error

def alert_dialog(msg):
    dialog=tkinter.Tk()
    tkinter.messagebox.showinfo("error message",msg)
    dialog.mainloop()

def add_data():
    

def make_connection():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            user='root',
                                            password='root',
                                            port=3307)
        return alert_dialog(connection)
        

    except Error as e:
       return alert_dialog(e)
if __name__=="__main__":
    make_connection()
