from tkinter import *
from tkinter import messagebox
import sqlite3 

con = sqlite3.connect('database.db')
cur =  con.cursor()

class Display(Toplevel): 

    def __init__(self,person_id):
        Toplevel.__init__(self)
        
        self.geometry("650x550+600+200")
        self.title("Display person")
        self.resizable(False,False)


        print("person_id =", person_id)
        query = "select * from addressbook where person_id= '{}'".format(person_id)
        result = cur.execute(query).fetchone()
        print(result)
        self.person_id = person_id

        Person_fullname = result[1]
        person_gender = result[2]
        person_email = result[3]
        person_phone = result[4]
        person_address = result[5]
          
        print("person name:",Person_fullname)





        self.top = Frame(self,height="150",bg="white")
        self.top.pack(fill=X)
        
        self.bottom = Frame(self,heigh='500',bg='powder blue')
        self.bottom.pack(fill = X)

        # Image
        self.top_img = PhotoImage(file='icon/people.png')
        self.top_img_label = Label(self.top,image=self.top_img,bg='white')
        self.top_img_label.place(x=70,y=25)


        #Heading
        self.top_heading = Label(self.top,text="Person Details",font="arial 20 bold",bg = 'white', fg="#ebb434")
        self.top_heading.place(x=150,y=30)
        
        # name 
        self.name = Label(self.bottom,text="Name",font="arial 15 bold")
        self.name.place (x=40,y=40)

        self.name_entry = Entry(self.bottom,width=30,bd=4)
        self.name_entry.insert(0,"enter name")
        self.name_entry.place(x=150,y=40)
        
        # Name

        self.name = Label(self.bottom,text="Name:",font="arial 15 bold",bg="powder blue")
        self.name.place (x=40,y=40)
        #Name Entyr
        self.name_entry = Entry(self.bottom,width=30,bd=4)
        self.name_entry.insert(0,Person_fullname)
        self.name_entry.config(state='disabled')
        self.name_entry.place(x=150,y=40)
        # Sure Name
        self.gender = Label(self.bottom,text="Gender:",font ="arial 15 bold",bg="powder blue")
        self.gender.place(x=40,y=80)
        #Sure_name Entry
        self.gender_entry = Entry(self.bottom,width=30,bd=4)
        self.gender_entry.insert(0,person_gender)
        self.gender_entry.config(state='disabled')
        self.gender_entry.place(x=150,y=80)
        #Email
        self.email = Label(self.bottom,text='Email:',font = "arial 15 bold",bg ="powder blue" )
        self.email.place(x = 40,y=120)
        #email entry
        self.email_entry = Entry(self.bottom,widt=30,bd = 4)
        self.email_entry.insert(0,person_email)
        self.email_entry.config(state='disabled')
        self.email_entry.place(x=150,y=120)
        #  Phone number
        self.phone  = Label(self.bottom,text="Phone:",font = "arial 15 bold",bg = "powder blue")
        self.phone.place(x=40,y=160)
        #Phone Entry
        self.phone_entry = Entry(self.bottom,bd =4,width=30)
        self.phone_entry.insert(0,person_phone)
        self.phone_entry.config(state='disabled')
        self.phone_entry.place(x=150,y=160)
       
        #Address 
        self.address  = Label(self.bottom,text="Address:",font = "arial 15 bold",bg = "powder blue")
        self.address.place(x=40,y=200)

        #Phone Entry
        self.address_entry = Text(self.bottom,bd = 4,width=30,height=6)
        self.address_entry.insert(1.0,person_address)
        self.address_entry.config(state='disabled')
        self.address_entry.place(x=150,y=200)

        self.botton = Button(self.bottom,text="Exit",bd=5,command = self.destroy)
        self.botton.place(x=300,y = 335)