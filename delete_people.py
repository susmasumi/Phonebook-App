from tkinter import *
from tkinter import messagebox
import sqlite3 

con = sqlite3.connect('database.db')
cur =  con.cursor()

class clear(Toplevel): 

    def __init__(self,person_id):
        Toplevel.__init__(self)
        
        self.geometry("650x550+600+200")
        self.title("Delete People")
        self.resizable(False,False)



        query = "DELETE from addressbook WHERE person_id = {}".format(person_id)

        try:
            cur.execute(query)
            con.commit()
            messagebox.showinfo("Success","Contact Deleted")
            self.destroy()
        except Exception as e:
            print(e)
