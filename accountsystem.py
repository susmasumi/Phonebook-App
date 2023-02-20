import re
from tkinter import *
from tkinter import messagebox
import sqlite3
from twilio.rest import Client
import os 

# Your Twilio account SID and AUTH token
account_sid = "AC387e3d62eadb80bb27f3466ed2d7848f"
auth_token = "b818fbab218bf71b4e4446a38f7ca1cd" 

# Create a Twilio client
client = Client(account_sid, auth_token)

# Your Twilio phone number
from_number = "+15095122518"
# Windows Size and Placement

AccountSystem = Tk()
AccountSystem.rowconfigure(0, weight=1)
AccountSystem.columnconfigure(0, weight=1)
height = 650
width = 1240
x=(AccountSystem.winfo_screenwidth()//2)-(width//2) 
y=(AccountSystem.winfo_screenheight()//4)-(height//4)
AccountSystem.geometry('{}x{}+{}+{}'.format(width, height, x, y))

AccountSystem.title("Account System")
# Navigating though windows
sign_in = Frame(AccountSystem)
sign_up = Frame(AccountSystem)

for frame in (sign_in, sign_up):
    frame.grid(row=0, column=0, sticky='nsew')
def show_frame(frame):
    frame.tkraise()

show_frame(sign_in)


email = StringVar()
password = StringVar()

# ================Login page Start Here ====================
sign_in.configure(bg="#525561")

# ================Background Image ====================
Login_backgroundImage = PhotoImage(file="assets//login.png")
bg_imageLogin = Label(
    sign_in,
    image=Login_backgroundImage,
    bg="#525561"
)
bg_imageLogin.place(x=120, y=28)


# ================ Header Text Left ====================
Login_headerText_image_left = PhotoImage(file="assets//headerText_image.png")
Login_headerText_image_label1 = Label(
    bg_imageLogin,
    image=Login_headerText_image_left,
    bg="#FFFFFF"
)
Login_headerText_image_label1.place(x=60, y=45)

Login_headerText1 = Label(
    bg_imageLogin,
    text="Phonebook App",
    fg="#000000",
    font=("yu gothic ui bold", 20 * -1),
    bg="#FFFFFF"
)
Login_headerText1.place(x=110, y=45)

# ================ Header Text Right ====================
Login_headerText_image_right = PhotoImage(file="assets//headerText_image.png")
Login_headerText_image_label2 = Label(
    bg_imageLogin,
    image=Login_headerText_image_right,
    bg="#FFFFFF"
)
Login_headerText_image_label2.place(x=400, y=45)

Login_headerText2 = Label(
    bg_imageLogin,
    anchor="nw",
    text="By Computing C 33",
    fg="#000000",
    font=("yu gothic ui Bold", 20 * -1),
    bg="#FFFFFF"
)
Login_headerText2.place(x=450, y=45)

# ================ LOGIN TO ACCOUNT HEADER ====================
loginAccount_header = Label(
    bg_imageLogin,
    text="Login to continue",
    fg="#000000",
    font=("yu gothic ui Bold", 28 * -1),
    bg="#FFFFFF"
)
loginAccount_header.place(x=75, y=121)

# ================ NOT A MEMBER TEXT ====================
loginText = Label(
    bg_imageLogin,
    text="Not a member?",
    fg="#000000",
    font=("yu gothic ui Regular", 15 * -1),
    bg="#FFFFFF"
)
loginText.place(x=75, y=187)

# ================ GO TO SIGN UP ====================
switchSignup = Button(
    bg_imageLogin,
    text="Sign Up",
    fg="#000000",
    font=("yu gothic ui Bold", 15 * -1),
    bg="#FFFFFF",
    bd=2,
    cursor="hand2",
    activebackground="#272A37",
    activeforeground="#ffffff",
    command=lambda: show_frame(sign_up)
)
switchSignup.place(x=220, y=185, width=70, height=35)


# ================ Email Name Section ====================
Login_emailName_image = PhotoImage(file="assets//email.png")
Login_emailName_image_Label = Label(
    bg_imageLogin,
    image=Login_emailName_image,
    bg="#FFFFFF"
    
)
Login_emailName_image_Label.place(x=76, y=242)

Login_emailName_text = Label(
    Login_emailName_image_Label,
    text="Email account",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
Login_emailName_text.place(x=25, y=0)

Login_emailName_icon = PhotoImage(file="assets//email-icon.png")
Login_emailName_icon_Label = Label(
    Login_emailName_image_Label,
    image=Login_emailName_icon,
    bg="#3D404B"
)
Login_emailName_icon_Label.place(x=370, y=15)

Login_emailName_entry = Entry(
    Login_emailName_image_Label,
    bd=2,
    bg="#FFFFFF",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    textvariable=email,

)
Login_emailName_entry.place(x=8, y=17, width=354, height=27)


# ================ Password Name Section ====================
Login_passwordName_image = PhotoImage(file="assets//email.png")
Login_passwordName_image_Label = Label(
    bg_imageLogin,
    image=Login_passwordName_image,
    bg="#FFFFFF"
)
Login_passwordName_image_Label.place(x=80, y=330)

Login_passwordName_text = Label(
    Login_passwordName_image_Label,
    text="Password",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
Login_passwordName_text.place(x=25, y=0)

Login_passwordName_icon = PhotoImage(file="assets//pass-icon.png")
Login_passwordName_icon_Label = Label(
    Login_passwordName_image_Label,
    image=Login_passwordName_icon,
    bg="#3D404B"
)
Login_passwordName_icon_Label.place(x=370, y=15)

Login_passwordName_entry = Entry(
    Login_passwordName_image_Label,
    bd=2,
    bg="#FFFFFF",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    textvariable=password,
)
Login_passwordName_entry.place(x=8, y=17, width=354, height=27)

# =============== Submit Button ====================
Login_button_image_1 = PhotoImage(
    file="assets//button_1.png")
Login_button_1 = Button(
    bg_imageLogin,
    image=Login_button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:login(),
    relief="flat",
    activebackground="#272A37",
    cursor="hand2",
)
Login_button_1.place(x=120, y=445, width=333, height=65)

# ================ Header Text Down ====================
Login_headerText_image_down = PhotoImage(file="assets//headerText_image.png")
Login_headerText_image_label3 = Label(
    bg_imageLogin,
    image=Login_headerText_image_down,
    bg="#FFFFFF"
)
Login_headerText_image_label3.place(x=650, y=530)

Login_headerText3 = Label(
    bg_imageLogin,
    text="Powered by Batch33",
    fg="#000000",
    font=("yu gothic ui bold", 20 * -1),
    bg="#FFFFFF"
)
Login_headerText3.place(x=700, y=530)


# ================ clear loginfiled ====================
def clear_login():
    email.set("")
    password.set("")


# ================ Database connection ====================

def login():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    find_user = "SELECT * FROM users WHERE email = ? AND password = ?"
    cursor.execute(find_user, [(Login_emailName_entry.get()), (Login_passwordName_entry.get())])
 
    result = cursor.fetchall()

    if result:
        messagebox.showinfo("Success", "Login Successfull")
        clear_login()
        # Store the session data
        with open("session.txt", "w") as file:
            file.write(Login_emailName_entry.get())
        AccountSystem.destroy()
        os.system("python main.py")
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

# ================ Forgot Password ====================
forgotPassword = Button(
    bg_imageLogin,
    text="Forgot Password",
    fg="#206DB4",
    font=("yu gothic ui Bold", 15 * -1),
    bg="#FFFFFF",
    bd=2,
    activebackground="#FFFFFF",
    activeforeground="#ffffff",
    cursor="hand1",
    command=lambda: forgot_password(),
)
forgotPassword.place(x=210, y=400, width=150, height=35)


def forgot_password():

    win = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    win.title('Forgot Password')
    # win.iconbitmap('images//aa.ico')
    win.configure(background='#272A37')
    win.resizable(False, False)

    # ====== Email ====================
    email_entry3 = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1,
                         bd=2)
    email_entry3.place(x=40, y=80, width=256, height=50)
    email_entry3.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    email_label3 = Label(win, text='• Email', fg="#FFFFFF", bg='#272A37',
                         font=("yu gothic ui", 11, 'bold'))
    email_label3.place(x=40, y=50)

    # ====  New Password ==================
    new_password_entry = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), show='•', highlightthickness=1,
                               bd=2)
    new_password_entry.place(x=40, y=180, width=256, height=50)
    new_password_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    new_password_label = Label(win, text='• New Password', fg="#FFFFFF", bg='#272A37',
                               font=("yu gothic ui", 11, 'bold'))
    new_password_label.place(x=40, y=150)

    # ======= Update password Button ============
    update_pass = Button(win, fg='#f8f8f8', text='Update Password', bg='#1D90F5', font=("yu gothic ui", 12, "bold"),
                         cursor='hand2', relief="flat", bd=2, highlightthickness=0, activebackground="#1D90F5",
                         command=lambda: change_password(email_entry3, new_password_entry))
    update_pass.place(x=40, y=260, width=256, height=45)

# database connection

def change_password(email_entry3, new_password_entry):
    email = email_entry3.get()
    password = new_password_entry.get()
    
    if email == "" or password == "":
        messagebox.showerror("Error", "All fields are required")
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror("Error", "Invalid email format")
        forgot_password()
    else:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        query = 'select * from users where email = ?'
        cursor.execute(query, [(email)])
        rows = cursor.fetchall()
        if not rows:
            messagebox.showerror("Error", "Email does not exist")
            forgot_password()
        else:
            phone_number = rows[0][2]
            name = rows[0][1]
            query = 'update users set password = ? where email = ?'
            cursor.execute(query, [(password), (email)])
            conn.commit()
             # Phone number in international format
            body = f"Dear {name}, your Phonebook account password has been changed for Email: {email_entry3.get()}. Your new password is: {new_password_entry.get()} Thank you for being a member, enjoy our services."
            client.messages.create(to=phone_number, from_=from_number, body=body)
            messagebox.showinfo("Success", "Password Updated Successfully")
            

            








# signup text variables
Name=StringVar()
number=StringVar()
email=StringVar()
password=StringVar()
confirm_password=StringVar()






# ================Signup page Start Here ====================
sign_up.configure(bg="#525561")

# ================Background Image ====================
backgroundImage = PhotoImage(file="assets//image_1.png")
bg_image = Label(
    sign_up,
    image=backgroundImage,
    bg="#525561"
)
bg_image.place(x=120, y=28)

# ================ Header Text Left ====================
headerText_image_left = PhotoImage(file="assets//headerText_image.png")
headerText_image_label1 = Label(
    bg_image,
    image=headerText_image_left,
    bg="#FFFFFF"
)
headerText_image_label1.place(x=60, y=45)

headerText1 = Label(
    bg_image,
    text="Phonebook App",
    fg="#000000",
    font=("yu gothic ui bold", 20 * -1),
    bg="#FFFFFF"
)
headerText1.place(x=110, y=45)

# ================ Header Text Right ====================
headerText_image_right = PhotoImage(file="assets//headerText_image.png")
headerText_image_label2 = Label(
    bg_image,
    image=headerText_image_right,
    bg="#FFFFFF"
)
headerText_image_label2.place(x=400, y=45)

headerText2 = Label(
    bg_image,
    anchor="nw",
    text="By Computing C 33",
    fg="#000000",
    font=("yu gothic ui Bold", 20 * -1),
    bg="#FFFFFF"
)
headerText2.place(x=450, y=45)

# ================ CREATE ACCOUNT HEADER ====================
createAccount_header = Label(
    bg_image,
    text="Create new account",
    fg="#000000",
    font=("yu gothic ui Bold", 28 * -1),
    bg="#FFFFFF"
)
createAccount_header.place(x=75, y=121)

# ================ ALREADY HAVE AN ACCOUNT TEXT ====================
text = Label(
    bg_image,
    text="Already a member?",
    fg="#000000",
    font=("yu gothic ui Regular", 15 * -1),
    bg="#FFFFFF"
)
text.place(x=75, y=187)

# ================ GO TO LOGIN ====================
switchLogin = Button(
    bg_image,
    text="Login",
    fg="#000000",
    font=("yu gothic ui Bold", 15 * -1),
    bg="#FFFFFF",
    bd=2,
    cursor="hand2",
    activebackground="#272A37",
    activeforeground="#ffffff",
    command=lambda: show_frame(sign_in)
)
switchLogin.place(x=230, y=185, width=50, height=35)

# ================ First Name Section ====================
Name_image = PhotoImage(file="assets//input_img.png")
Name_image_Label = Label(
    bg_image,
    image=Name_image,
    bg="#FFFFFF"
)
Name_image_Label.place(x=80, y=242)

Name_text = Label(
    Name_image_Label,
    text="Name",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
    
)
Name_text.place(x=25, y=0)

Name_icon = PhotoImage(file="assets//name_icon.png")
Name_icon_Label = Label(
    Name_image_Label,
    image=Name_icon,
    bg="#3D404B"
)
Name_icon_Label.place(x=159, y=15)

Name_entry = Entry(
    Name_image_Label,
    bd=2,
    bg="#FFFFFF",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    textvariable=Name
)
Name_entry.place(x=8, y=17, width=140, height=27)


# ================ number Section ====================
number_image = PhotoImage(file="assets//input_img.png")
number_image_Label = Label(
    bg_image,
    image=number_image,
    bg="#FFFFFF"
)
number_image_Label.place(x=293, y=242)

number_text = Label(
    number_image_Label,
    text="Phone Number",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
number_text.place(x=25, y=0)


number_icon = PhotoImage(file="assets//name_icon.png")
number_icon_Label = Label(
    number_image_Label,
    image=number_icon,
    bg="#3D404B"
)
number_icon_Label.place(x=159, y=15)

number_entry = Entry(
    number_image_Label,
    bd=2,
    bg="#FFFFFF",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    textvariable=number
)
number_entry.insert(0, "+977")
number_entry.place(x=8, y=17, width=140, height=27)

# ================ Email Name Section ====================
emailName_image = PhotoImage(file="assets//email.png")
emailName_image_Label = Label(
    bg_image,
    image=emailName_image,
    bg="#FFFFFF"
)
emailName_image_Label.place(x=80, y=311)

emailName_text = Label(
    emailName_image_Label,
    text="Email account",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
emailName_text.place(x=25, y=0)

emailName_icon = PhotoImage(file="assets//email-icon.png")
emailName_icon_Label = Label(
    emailName_image_Label,
    image=emailName_icon,
    bg="#3D404B"
)
emailName_icon_Label.place(x=370, y=15)

emailName_entry = Entry(
    emailName_image_Label,
    bd=2,
    bg="#FFFFFF",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    textvariable=email

)
emailName_entry.place(x=8, y=17, width=354, height=27)


# ================ Password Name Section ====================
passwordName_image = PhotoImage(file="assets//input_img.png")
passwordName_image_Label = Label(
    bg_image,
    image=passwordName_image,
    bg="#FFFFFF"
)
passwordName_image_Label.place(x=80, y=380)

passwordName_text = Label(
    passwordName_image_Label,
    text="Password",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
passwordName_text.place(x=25, y=0)

passwordName_icon = PhotoImage(file="assets//pass-icon.png")
passwordName_icon_Label = Label(
    passwordName_image_Label,
    image=passwordName_icon,
    bg="#3D404B"
)
passwordName_icon_Label.place(x=159, y=15)

passwordName_entry = Entry(
    passwordName_image_Label,
    bd=2,
    bg="#FFFFFF",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    textvariable=password,
)
passwordName_entry.place(x=8, y=17, width=140, height=27)


# ================ Confirm Password Name Section ====================
confirm_passwordName_image = PhotoImage(file="assets//input_img.png")
confirm_passwordName_image_Label = Label(
    bg_image,
    image=confirm_passwordName_image,
    bg="#FFFFFF"
)
confirm_passwordName_image_Label.place(x=293, y=380)

confirm_passwordName_text = Label(
    confirm_passwordName_image_Label,
    text="Confirm Password",
    fg="#FFFFFF",
    font=("yu gothic ui SemiBold", 13 * -1),
    bg="#3D404B"
)
confirm_passwordName_text.place(x=25, y=0)

confirm_passwordName_icon = PhotoImage(file="assets//pass-icon.png")
confirm_passwordName_icon_Label = Label(
    confirm_passwordName_image_Label,
    image=confirm_passwordName_icon,
    bg="#3D404B"
)
confirm_passwordName_icon_Label.place(x=159, y=15)

confirm_passwordName_entry = Entry(
    confirm_passwordName_image_Label,
    bd=2,
    bg="#FFFFFF",
    highlightthickness=0,
    font=("yu gothic ui SemiBold", 16 * -1),
    textvariable=confirm_password
)
confirm_passwordName_entry.place(x=8, y=17, width=140, height=27)

# =============== Submit Button ====================
submit_buttonImage = PhotoImage(
    file="assets//button_1.png")
submit_button = Button(
    bg_image,
    image=submit_buttonImage,
    borderwidth=0,
    command=lambda: signup(),
    highlightthickness=0,
    relief="flat",
    activebackground="#272A37",
    cursor="hand2",
)
submit_button .place(x=130, y=460, width=333, height=65)

# ================ Header Text Down ====================
headerText_image_down = PhotoImage(file="assets//headerText_image.png")
headerText_image_label3 = Label(
    bg_image,
    image=headerText_image_down,
    bg="#FFFFFF"
)
headerText_image_label3.place(x=650, y=530)

headerText3 = Label(
    bg_image,
    text="Powered by Batch33",
    fg="#000000",
    font=("yu gothic ui bold", 20 * -1),
    bg="#FFFFFF"
)
headerText3.place(x=700, y=530)

def clear():
    Name.set("")
    number.set("")
    email.set("")
    password.set("")
    confirm_password.set("")

# ================ Database connection ====================
def signup():
    # Check if all required fields are filled
    if Name_entry.get() == "" or number_entry.get() == "" or emailName_entry.get() == "" or passwordName_entry.get() == "" or confirm_passwordName_entry.get() == "":
        messagebox.showerror("Error", "All fields are required")
        return

    # Check if password and confirm password match
    elif passwordName_entry.get() != confirm_passwordName_entry.get():
        messagebox.showerror("Error", "Password and Confirm Password should be same")
        return

    # Check if the email is in correct format
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", emailName_entry.get()):
        messagebox.showerror("Error", "Invalid email address")
        return

    else:
        try:
            connection = sqlite3.connect("database.db")
            cursor = connection.cursor()
            
            # Check if the email already exists in the database
            cursor.execute("SELECT * FROM users WHERE email=?", (emailName_entry.get(),))
            email_exists = cursor.fetchone()
            if email_exists:
                messagebox.showerror("Error", "Email already exists")
                return

            # Insert new user into the database
            cursor.execute("INSERT INTO users(Name, Phonenumber, email, password) VALUES(?, ?, ?, ?)", (Name_entry.get(), number_entry.get(), emailName_entry.get(), passwordName_entry.get()))
            to_number = number_entry.get()
             # Phone number in international format
            body = f"Greetings {Name_entry.get()}! Your Phonebook account has been successfully created with email: {emailName_entry.get()} and password: {passwordName_entry.get()}. We are thrilled to have you as a member. Enjoy our services!"
            client.messages.create(to=to_number, from_=from_number, body=body)
            connection.commit()
            connection.close()
            clear()
            messagebox.showinfo("Success", "Account has been created successfully")
             # Send an SMS to the user's phone number with their credentials and a thank you message
            
        except Exception as es:
            messagebox.showerror("Error", f"Error due to: {str(es)}")
AccountSystem.resizable(False, False)
AccountSystem.mainloop() 
