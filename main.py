from tkinter import *

#RIGHT SIDE WINDOW#
def show_content(screen):
    for widget in right_frame.winfo_children():
        widget.destroy()
    
    #PANIC RIGHT SIDE WINDOW#
    if screen == "panic":
        Label(right_frame,
               text="Emergency panic button",
               font=("Arial", 20, "bold"),
               bg="#f2f2f2").pack(pady=40)
        
        Button(right_frame,
               text="Deactivate Panic Button",
               font=("Arial", 14, "bold"),
               bg="#b71c1c",
                fg="white",
               padx=20,
               pady=10).pack()
        
    if screen == "instructions":
        Label(right_frame,
                text = "This is the emergency section",
                font = ("Arial", 20, "bold"),
                bg = "#f2f2f2").pack(pady=40)
        
    if screen == "hotlines":
        Label(right_frame,
                text = "This is the hotlines section",
                font = ("Arial", 20, "bold"),
                bg = "#f2f2f2").pack(pady=40)
        
    if screen == "add_hotlines":
        Label(right_frame,
                text = "This is the add hotlines section",
                font = ("Arial", 20, "bold"),
                bg = "#f2f2f2").pack(pady=40)
        
    if screen == "about":
        Label(right_frame,
                text = "This is the about section",
                font = ("Arial", 20, "bold"),
                bg = "#f2f2f2").pack(pady=40)
              
#-------------------------------------#

#WINDOW FOR PANIC BUTTON, SIZE, TITLE#
window = Tk()
window.geometry("1080x720")
window.title("Protectly")

#SIDEBAR#
sidebar = Frame(window,
            bg="#b71c1c",
            width=350)

sidebar.pack(side="left",
            fill="y"),
sidebar.pack_propagate(False)

#SIDEBAR NAME#
sidebar_name = Label(sidebar,
            text="Protectly: Emegency Safety App",
            bg="#b71c1c",
            fg="white",
            font=("Arial", 16, "bold"))
sidebar_name.pack(pady=30)

#SIDEBAR ROOF#
sidebar_roof = Frame(window,
                bg="#b71c1c",
                height=30)
sidebar_roof.pack(side="top",fill="x")

right_frame = Frame(window, bg="#ffffff")
right_frame.pack(side="right", fill="both", expand=True)

#-------------------------------------#

#EMEGENCY PANIC BUTTON#
panic_button = Button(sidebar,
                text="Emergency Panic Button")
panic_button.config(font=('Sans-serif', 14, "bold"))
panic_button.config(bg="#b71c1c")
panic_button.config(fg="#ffffff")
panic_button.config(command=lambda: show_content("panic"))
panic_button.pack(pady=20,padx=30,fill="x")

#INSTRUCTIONS BUTTON#
instructions_button = Button(sidebar,
                text="Emergency Instructions")
instructions_button.config(font=('Sans-serif', 14, 'bold'))
instructions_button.config(bg="#b71c1c")
instructions_button.config(fg="#ffffff")
instructions_button.config()
instructions_button.config(command=lambda: show_content("instructions"))
instructions_button.pack(pady=20,padx=30,fill="x")

#HOTLINES LIST BUTTON#
hotlines_button = Button(sidebar,
                text="Hotlines List")
hotlines_button.config(font=('Sans-serif', 14, "bold"))
hotlines_button.config(bg="#b71c1c")
hotlines_button.config(fg="#ffffff")
hotlines_button.config(command=lambda: show_content("hotlines"))
hotlines_button.pack(pady=20,padx=30,fill="x")

#ADD HOTLINES BUTTON#
add_hotlines = Button(sidebar,
                text="Add Hotlines")
add_hotlines.config(font=('Sans-serif',14,"bold"))
add_hotlines.config(bg="#b71c1c")
add_hotlines.config(fg="#ffffff")
add_hotlines.config(command=lambda: show_content("add_hotlines"))
add_hotlines.pack(pady=20,padx=30,fill="x")

#ABOUT BUTTON#
about_button = Button(sidebar,
                text="About Protectly")
about_button.config(font=('Sans-serif',14,"bold"))
about_button.config(bg="#b71c1c")
about_button.config(fg="#ffffff")
about_button.config(command=lambda: show_content("about"))
about_button.pack(pady=20,padx=30,fill="x")

window.mainloop()