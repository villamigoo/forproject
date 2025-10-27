from tkinter import *

window = Tk()

label1 = Label(window,text="Hello")
label2 = Label(window,text="Im workiong on python")

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

window.mainloop()