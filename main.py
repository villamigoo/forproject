from tkinter import *
from PIL import Image, ImageTk

#ALERT MESSAGE WHEN BUTTON IS PRESSED#
def create_window():
    new_window = Toplevel()
    new_window.title("Panic Window")
    new_window.geometry("400x80")

    label = Label(
                new_window,
                text="Parents/Guardians have been contacted!",
                font=('Arial', 12, 'bold'),
                fg="#b71c1c")
    label.place(x=45, y=25)
    
#OPENS FIRE INSTRUCTIONS#
def fire_create_window():
    fire_window = Toplevel()
    fire_window.title("Fire Window")
    fire_window.geometry("600x720")

    fire_image = Image.open("fire_emergency.png")
    fire_photo = ImageTk.PhotoImage(fire_image)
    label = Label(fire_window,
                text="Test for fire", 
                image=fire_photo,
                compound="top",
                font=("Arial",12,"bold"))
    label.image = fire_photo
    label.pack()

#OPENS MEDICAL INSTRUCTIONS#
def medical_create_window():
    medical_window = Toplevel()
    medical_window.title("Medical")
    medical_window.geometry("600x720")

    medical_image = Image.open("medical_emergencyy.png")
    medical_photo = ImageTk.PhotoImage(medical_image)
    label = Label(medical_window,
                  text="Test for Medical",
                  image=medical_photo,
                  compound="top",
                  font=("Arial",12,"bold"))
    label.image = medical_photo
    label.pack()

def disaster_create_window():
    disaster_window = Toplevel()
    disaster_window.title("Disaster")
    disaster_window.geometry("600x720")
   
    image = Image.open("natural_disaster.png")  
    photo = ImageTk.PhotoImage(image)
    label = Label(disaster_window,
                  text="Test for disaster",
                  image=photo,
                  compound="top",  
                  font=("Arial", 12, "bold"))
    label.image = photo
    label.pack()

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
                command=create_window,  
                font=("Arial", 14, "bold"),
                bg="#b71c1c",
                fg="white").place(x=235, y=250)
        
#SWITCHES TO INSTRUCTIONS WINDOW#
    if screen == "instructions":
        Label(right_frame,
                text = "This is the emergency section",
                font = ("Arial", 20, "bold"),
                bg = "#f2f2f2").pack(pady=40)
        
        Button(right_frame,
                text="Fire",
                command=fire_create_window,
                font=("Arial", 14, "bold"),
                bg="#b71c1c",
                fg="white").place(x=70, y=150)
        
        Button(right_frame,
                text="Medical",
                command=medical_create_window,
                font=("Arial", 14, "bold"),
                bg="#b71c1c",
                fg="white").place(x=150, y=150)
        
        Button(right_frame,
                text="Natural Disaster",
                command=disaster_create_window,
                font=("Arial", 14, "bold"),
                bg="#b71c1c",
                fg="white").place(x=250, y=150)
        
#SWITCHES TO HOTLINES LIST WINDOW#
    if screen == "hotlines":
        Label(right_frame,
                text = "This is the hotlines section",
                font = ("Arial", 20, "bold"),
                bg = "#f2f2f2").pack(pady=40)

#SWITCHES TO ADD HOTLINES WINDOW#
    if screen == "add_hotlines":
        Label(right_frame,
                text = "This is the add hotlines section",
                font = ("Arial", 20, "bold"),
                bg = "#f2f2f2").pack(pady=40)

#SWITCHES TO ABOUT WINDOW#
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