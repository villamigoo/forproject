from tkinter import *

#Opens a new window for the alert message
def create_window():
    new_window = Toplevel()
    new_window.title("Alert")
    new_window.geometry("200x110")


window = Tk()
window.geometry("520x520")
window.title("Protectly")
#Pag priness yung button magpapakita yung alert message. lagyan niyo ng message yung popup
button = Button(window,text='Emergency Panic Button',command=create_window) 
button.config(font=('Impact',20,'bold'))
button.config(fg='red')
image =PhotoImage(file='emergency.png').subsample(4,4)
button.config(image=image)
button.config(compound='top')
button.pack(pady=150)
window.mainloop()