from tkinter import *
from PIL import Image, ImageTk
from utils import windows

#RIGHT SIDE WINDOW#
def show_content(screen):
    for widget in right_frame.winfo_children():
        widget.destroy()
    
#SWITCHES TO PANIC WINDOW#
    if screen == "panic":
        Label(right_frame,
                text="Emergency panic button",
                font=("Arial", 20, "bold"),
                bg="#f2f2f2").pack(pady=40)
        
        Button(right_frame,
                text="⚠️Activate Panic Button⚠️",
                command= windows.create_window,  
                font=("Arial", 14, "bold"),
                bg="#b71c1c",
                fg="white",
                height=2).place(x=235, y=250)
        
#SWITCHES TO DIFFERENT WINDOWS#
    elif screen == "instructions":
        Label(right_frame,
                text = "This is the emergency section\nClick a button to see the emergency instructions based on the category.",
                font = ("Arial", 15, "bold"),
                bg = "#f2f2f2").pack(pady=40)
        
        Button(right_frame,
                text="Fire",
                command=windows.fire_create_window,
                font=("Arial", 14, "bold"),
                bg="#b71c1c",
                fg="white",
                width=25).place(x=220, y=150)
    
        Button(right_frame,
                text="Medical",
                command=windows.medical_create_window,
                font=("Arial", 14, "bold"),
                bg="#b71c1c",
                fg="white",
                width=25).place(x=220, y=210)
    
        Button(right_frame,
                text="Natural Disaster",
                command=windows.disaster_create_window,
                font=("Arial", 14, "bold"),
                bg="#b71c1c",
                fg="white",
                width=25).place(x=220, y=270)
        
#SWITCHES TO HOTLINES LIST WINDOW#
    elif screen == "hotlines":
        Label(right_frame,
          text="Hotlines List",
          font=("Arial", 20, "bold"),
          bg="#f2f2f2").pack(pady=20)

        try:
            with open("hotlineslist.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()

            for hotline in lines:
                Label(right_frame,
                    text=hotline.strip(),
                    font=("Arial", 14),
                    bg="#f2f2f2",
                    anchor="w").pack(anchor="w", padx=50, pady=5)

        except FileNotFoundError:
            Label(right_frame,
                text="Hotlines file not found.",
                font=("Arial", 14),
                bg="#f2f2f2",
                fg="red").pack(pady=20)

#SWITCHES TO ADD HOTLINES WINDOW#
    elif screen == "add_hotlines":
        Label(right_frame,
                text = "This is the add hotlines section",
                font = ("Arial", 20, "bold"),
                bg = "#f2f2f2").pack(pady=40)

#SWITCHES TO ABOUT WINDOW#
    elif screen == "about":
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
                text="Emergency Panic Button",
                font=("Sans-serif",14,"bold"),
                bg="#b71c1c",
                fg="#ffffff",
                command=lambda: show_content("panic"))
panic_button.pack(pady=20,padx=30,fill="x")

#INSTRUCTIONS BUTTON#
instructions_button = Button(sidebar,
                text="Emergency Instructions",
                font=("Sans-serif", 14, "bold"),
                bg="#b71c1c",
                fg="#ffffff",
                command=lambda: show_content("instructions"))
instructions_button.pack(pady=20,padx=30,fill="x")

#HOTLINES LIST BUTTON#
hotlines_button = Button(sidebar,
                text="Hotlines List",
                font=("Sans-serif", 14, "bold"),
                bg="#b71c1c",
                fg="#ffffff",
                command=lambda: show_content("hotlines"))
hotlines_button.pack(pady=20,padx=30,fill="x")

#ADD HOTLINES BUTTON#
add_hotlines = Button(sidebar,
                text="Add Hotlines",
                font=("Sans-serif",14,"bold"),
                bg="#b71c1c",
                fg="#ffffff",
                command=lambda: show_content("add_hotlines"))
add_hotlines.pack(pady=20,padx=30,fill="x")

#ABOUT BUTTON#
about_button = Button(sidebar,
                text="About Protectly",
                font=("Sans-serif",14,"bold"),
                bg="#b71c1c",
                fg="#ffffff",
                command=lambda: show_content("about"))
about_button.pack(pady=20,padx=30,fill="x")

window.mainloop()