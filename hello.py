from tkinter import *

def display():
    if(x.get()==1):
        print("I like python")
    else:
        print("I don't like python lesh")

window = Tk()

x = IntVar()

checkbox = Checkbutton(window, text='Python', variable=x,onvalue=1,offvalue=0,command=display)
checkbox.pack()
checkbox.config(font=('Arial',20))
checkbox.config(fg='#0000FF')
checkbox.config(bg='#000000')
window.mainloop()