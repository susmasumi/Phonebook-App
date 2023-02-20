from tkinter import *
from add_people import AddPeople
import sqlite3 
from update_people import Update
from display import Display
from delete_people import clear


con = sqlite3.connect('database.db')
cur =  con.cursor()

class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        
        self.geometry("650x550+600+200")
        self.title("My People")
        self.resizable(False,False)


        self.top = Frame(self,height="150",bg="white")
        self.top.pack(fill=X)
        
        self.bottom = Frame(self,heigh='500',bg='powder blue')
        self.bottom.pack(fill = X)

        # image
        self.top_img = PhotoImage(file='icon/peoples.png')
        self.top_img_label = Label(self.top,image=self.top_img,bg='white')
        self.top_img_label.place(x=70,y=25)

        #  heading
        self.top_heading = Label(self.top,text="My People",font="arial 20 bold",bg = 'white', fg="#ebb434")
        self.top_heading.place(x=150,y=30)
        
        self.scroll = Scrollbar(self.bottom, orient=VERTICAL)

        self.list_box = Listbox(self.bottom, width=40, height=21)
        self.list_box.grid(row=0,column=0, padx=(40,0))
        self.scroll.config(command=self.list_box.yview)
        self.list_box.config(yscrollcommand = self.scroll.set)


        persons = cur.execute("select * from 'addressbook'").fetchall()
        print(persons)
        
        count=0
        for person in persons:
            self.list_box.insert(count, str(person[0])+ ". " +person[1])
            count+=1
        self.scroll.grid(row=0,column=1,sticky=N+S)
       
        
        #Buttons
        self.btn_add = Button(self.bottom,text="Add",width=12,font='arial 11 bold',command=self.add_people)
        self.btn_add.grid(row=0,column=2,sticky=N,padx=20,pady=10)
        
        self.btn_update = Button(self.bottom,text="Update",width=12,font='arial 11 bold',
                 command = self.update_func)
        self.btn_update.grid(row=0,column=2,sticky=N,padx=20,pady=50,)
        
        self.btn_display=Button(self.bottom,text="Display",width=12,font="arial 11 bold",command = self.display_func)
        self.btn_display.grid(row=0,column=2,sticky=N,padx=20,pady=90)

        self.btn_delete = Button(self.bottom,text="Delete",width=12,font="arial 11 bold",command= self.clear_func)
        self.btn_delete.grid(row=0,column=2,sticky=N,padx=20,pady=130)
        
        self.btn_delete = Button(self.bottom,text="EXIT",width=12,font="arial 11 bold",command= self.destroy)
        self.btn_delete.grid(row=0,column=2,sticky=N,padx=20,pady=170)
        

    def add_people(self):
        add_new = AddPeople()
        self.destroy()


    def update_func(self):
        selected_item = self.list_box.curselection()
        person = self.list_box.get(selected_item)
        person_id = person.split('.')[0]
        updadate_page  = Update(person_id)
        
    def display_func(self):
        selected_item = self.list_box.curselection()
        person = self.list_box.get(selected_item)
        person_id = person.split('.')[0]
        display_page  = Display(person_id)

    def clear_func(self):
        selected_item = self.list_box.curselection()
        person = self.list_box.get(selected_item)
        person_id = person.split('.')[0]
        display_page  = clear(person_id) 
        self.destroy()
                                    
   

  