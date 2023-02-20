from tkinter import *

class aboutus(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        
        self.geometry("650x550+600+200")
        self.title("About Us")
        self.resizable(False,False)

        self.top = Frame(self, height=150, bg="white")
        self.top.pack(fill=X)
        
        self.bottom = Frame(self, height=400, bg='powder blue')
        self.bottom.pack(fill=X)
        
        # Top frame image
        self.top_image = PhotoImage(file="icon/aboutus.png", width=100, height=100)

        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=10, y=25)

        # Heading
        self.top_heading = Label(self.top, text="Hey,this is about us page", font="Arial 20 bold", bg='white', fg="#ebb434")
        self.top_heading.place(x=150, y=30)

        # About application
        self.about_label = Label(self.bottom, text="This application is developed by students of Softwarica College of IT and E-Commerce\n\n as a project for the Software Engineering course.The purpose of this application is to \n\nprovide a simple, user-friendly interface for managing contacts.\n\nFor more information about Softwarica College, \n\nplease visit our website or follow us on social media.",
                                 font="Arial 12", fg="#000000", bg='#34baeb', justify=CENTER)
        self.about_label.pack(pady=20)

        # Social media links
        self.social_media_label = Label(self.bottom, text="Follow us on social media:",
                                         font="Arial 15 bold", fg="#000000", bg='#34baeb')
        self.social_media_label.pack(pady=10)

        self.facebook_label = Label(self.bottom, text="Facebook: https://www.facebook.com/softwarica.nepal",
                                     font="Arial 12", fg="#000000", bg='#34baeb', justify=LEFT)
        self.facebook_label.pack()

        self.instagram_label = Label(self.bottom, text="Instagram: https://www.instagram.com/softwarica.college/",
                                      font="Arial 12", fg="#000000", bg='#34baeb', justify=LEFT)
        self.instagram_label.pack()

        self.website_label = Label(self.bottom, text="Website: http://softwarica.edu.np",
                                      font="Arial 12", fg="#000000", bg='#34baeb', justify=LEFT)
        self.website_label.pack()

        # Exit button
        self.exit_button = Button(self.bottom, text="Exit", command=self.destroy)
        self.exit_button.pack(pady=20)
