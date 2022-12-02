import tkinter as tk
from tkinter import *
import tkafterlogin


def submitact():
    user = username.get()
    passw = password.get()
    validate(user, passw)


def tkafterlogin():
    root2 = Toplevel(root)
    root2.geometry("200x100")
    root2.title("Logged in")

    l = tk.Label(root2, text="Logged in Successfully!").place(x=10, y=10)
    btn = tk.Button(root2, text="okay", command=root2.destroy)
    btn.place(x=75, y=50)


def validate(user, passw):
    if (user == "a" and passw == "a"):
        tkafterlogin()
    else:
        label.config(text="Unsuccessful")
        label.pack()


root = tk.Tk()
root.geometry("300x300")
root.title("DBMS Login Page")

label = Label(root, text="")
label.place(x=100, y=5)

lblfirstrow = tk.Label(root, text="Username")
lblfirstrow.place(x=50, y=20)

username = tk.Entry(root, width=35)
username.place(x=150, y=20, width=100)

lblsecondrow = tk.Label(root, text="Password")
lblsecondrow.place(x=50, y=50)

password = tk.Entry(root, width=35, show="*")
password.place(x=150, y=50, width=100)

submitbtn = tk.Button(root, text="Login", command=submitact)
submitbtn.place(x=150, y=135, width=55)

root.mainloop()
