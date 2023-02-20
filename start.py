from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
import os

root = Tk()
image = PhotoImage(file='assets//vector2.png')

height = 430
width = 530
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
#root.overrideredirect(True)

root.config(background="white")
welcome = Label(root, text="Welcome to the Phonebook.. ", font=("Trebuchet Ms", 13,"bold"), bg="white", fg="#000000")


bg_label = Label(root, image=image, bg="white")
bg_label.place(x=130, y=65)

progress_label = Label(root, text="Loading...", font=("Trebuchet Ms", 13,"bold"), bg="white", fg="#000000")
progress_label.place(x=190, y=330)

progress = Progressbar(root, orient=HORIZONTAL, length=400, mode='indeterminate', style="red.Horizontal.TProgressbar")
progress.place(x=60, y=370)

def top():
    root.withdraw()
    os.system('python accountsystem.py')
    root.destroy()
i = 0
def load():
    global i
    if i <= 5:
        txt='Loading...'+(str(20*i))+'%'
        progress_label.config(text=txt)
        progress_label.after(600, load)
        progress['value'] = 20*i
        i += 1
    else:
        top()
load()





root.resizable(False, False)
root.mainloop()
