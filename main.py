from tkinter import *
from view_people import MyPeople
from add_people import AddPeople
import datetime
from about_us import aboutus


class Application(object):
    def __init__(self,master):
        self.master = master

        self.top = Frame(master,height = 150, bg='white') # For Top Bar 
        self.top.pack(fill = X)                                                                     

        self.bottom = Frame(master,heigh=650,bg='#34baeb') # For Butto m bar
        self.bottom.pack(fill = X)

        # top frame Image 
        self.top_image = PhotoImage(file="icon/logo.png")
        self.top_image_label = Label(self.top, image = self.top_image,bg='white')
        self.top_image_label.place(x=70,y=25)

        # Heading
        self.top_heading = Label(self.top,text=" Phonebook",font="arial 20 bold",bg = 'white', fg="#ebb434")
        self.top_heading.place(x=150,y=30)

        # Date 
        date = datetime.datetime.now().date()
        date = str(date)
       
        # Showing Top manu
        self.date_label = Label(self.top, text="Today's Date:\n"+date,font="arial 15 bold",fg="#ebb434",bg="white")
        self.date_label.place(x=480,y=20)

        # View Button
        self.ViewButton = Button(self.bottom, text = "View People",font="arial 15 bold",bg='white',fg='#42bcf5',bd=4, command = self.my_people)
        self.ViewButton.place(x=250,y=70)

        # Add Button
        self.AddButton = Button(self.bottom, text = " Add People",font="arial 15 bold",bd=4,bg='white',fg='#42bcf5',command = self.add_people_func)
        self.AddButton.place(x=250,y=130)

        # About us
        self.AboutButton = Button(self.bottom, text = "   About us  ",font="arial 15 bold",bd=3,bg='white',fg='#42bcf5', command=self.about_us)
        self.AboutButton.place(x=250,y=190)

        # Exit Button
        self.add_exit_button()

    def my_people(self):
        people = MyPeople()

    def add_people_func(self):
        add_people_now = AddPeople()

    def about_us(self):
        about = aboutus()

    def exit_app(self):
        self.master.destroy()

    def add_exit_button(self):
        self.ExitButton = Button(self.bottom, text="Exit", font="arial 15 bold", bd=4, bg='RED', fg='#FFFFFF', command=self.exit_app)
        self.ExitButton.place(x=280, y=250)


def main():
    root = Tk()
    app = Application(root)
    root.title("PhoneBook App")
    root.geometry('650x550+350+250')
    root.resizable(False,False)
    # root.configure(bg = 'white')
    root.mainloop()

if __name__ == '__main__':
    main()

