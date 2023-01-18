from tkinter import *


root = Tk()
root.geometry("400x300")
root.resizable(0, 0)
root.title("Calculator")


def btn_click(item):
    global expression
    expression = expression + str(item)
    inputTxt.set(expression)


def bt_clear():
    global expression
    expression = ""
    inputTxt.set("")


def bt_equal():
    global expression
    result = str(eval(expression))
    inputTxt.set(result)
    expression = ""


expression = ""

inputTxt = StringVar(root)

inputFrame = Frame(root, width=400, height=50, bd=1,
                   highlightbackground="black", highlightcolor="black", highlightthickness=2)
inputFrame.pack(side=TOP)
inputField = Entry(inputFrame, font=('ariel', 16, 'bold'),
                   textvariable=inputTxt, width=50, bg="#eee", bd=1, justify=RIGHT)

inputField.grid(row=0, column=0)
inputField.pack(ipadx=4, ipady=4)

btnFrame = Frame(root, width=400, height=250, bg="white")
btnFrame.pack()

clear = Button(btnFrame, text="C", fg="black", width=41, height=3, bd=0,
               cursor="hand2", command=lambda: bt_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide = Button(btnFrame, text="/", fg="black", width=13, height=3, bd=0, cursor="hand2",
                command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)


seven = Button(btnFrame, text="7", fg="black", width=13, height=3, bd=0,
               cursor="hand2", command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)

eight = Button(btnFrame, text="8", fg="black", width=13, height=3, bd=0,
               cursor="hand2", command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)

nine = Button(btnFrame, text="9", fg="black", width=13, height=3, bd=0,
              cursor="hand2", command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)

multiply = Button(btnFrame, text="*", fg="black", width=13, height=3, bd=0,
                  cursor="hand2", command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)


four = Button(btnFrame, text="4", fg="black", width=13, height=3, bd=0,
              cursor="hand2", command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)

five = Button(btnFrame, text="5", fg="black", width=13, height=3, bd=0,
              cursor="hand2", command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)

six = Button(btnFrame, text="6", fg="black", width=13, height=3, bd=0, cursor="hand2",
             command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)

minus = Button(btnFrame, text="-", fg="black", width=13, height=3, bd=0,
               cursor="hand2", command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)


one = Button(btnFrame, text="1", fg="black", width=13, height=3, bd=0,
             cursor="hand2", command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)

two = Button(btnFrame, text="2", fg="black", width=13, height=3, bd=0,
             cursor="hand2", command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)

three = Button(btnFrame, text="3", fg="black", width=13, height=3, bd=0,
               cursor="hand2", command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)

plus = Button(btnFrame, text="+", fg="black", width=13, height=3, bd=0,
              cursor="hand2", command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)


zero = Button(btnFrame, text="0", fg="black", width=27, height=3, bd=0, cursor="hand2",
              command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

point = Button(btnFrame, text=".", fg="black", width=13, height=3, bd=0,
               cursor="hand2", command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)

equals = Button(btnFrame, text="=", fg="black", width=13, height=3, bd=0,
                cursor="hand2", command=lambda: bt_equal()).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()
