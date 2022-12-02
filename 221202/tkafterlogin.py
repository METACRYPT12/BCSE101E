import tkinter as tk
from tkinter import *


root = tk.Tk()
root.geometry("200x50")
root.title("Logged in")

lblfirstrow = tk.Label(root, text="Logged in Successfully!")
lblfirstrow.pack(side=TOP)
root.mainloop()
