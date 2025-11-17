from tkinter import *
from utils import windows
from utils import crud
import datetime

#COLORS#
SIDEBAR_COLOR = "dark red"
BUTTON_COLOR = "dark red"
BUTTON_TEXT_COLOR = "white"
TEXT_COLOR = "white"
WINDOW_COLOR ="white"

#ADDS THE TYPED NUMBER TO THE HOTLINES LIST WINDOW"
def add_hotline(entry):
    hotline = entry.get().strip()
    if hotline:
        with open("hotlineslist.txt", "a", encoding="utf-8") as file:
            file.write(hotline + "\n")
        entry.delete(0, END)
    show_content("add_hotlines")

def update_hotline(old_value, new_value):
    with open("hotlineslist.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open("hotlineslist.txt", "w", encoding="utf-8") as file:
        for line in lines:
            if line.strip() == old_value.strip():
                file.write(new_value + "\n")
            else:
                file.write(line)

def open_update_window(old_value):
    update_win = Toplevel()
    update_win.title("Update Hotline")
    update_win.geometry("400x200")

    Label(update_win, text="Update Hotline:", font=("Arial", 14)).pack(pady=10)

    entry = Entry(update_win, font=("Arial", 14), width=25)
    entry.pack(pady=5)
    entry.insert(0, old_value)

    def save_update():
        new_value = entry.get().strip()
        if new_value:
            update_hotline(old_value, new_value)
            show_content("add_hotlines")
            update_win.destroy()

    Button(update_win,
           text="Save",
           font=("Arial", 12, "bold"),
           bg=BUTTON_COLOR,
           fg=WINDOW_COLOR,
           command=save_update).pack(pady=10)

def delete_specific_hotline(hotline):
    with open("hotlineslist.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open("hotlineslist.txt", "w", encoding="utf-8") as file:
        for line in lines:
            if line.strip() != hotline:
                file.write(line)
    show_content("add_hotlines")

#RIGHT SIDE WINDOW#
def show_content(screen):
    for widget in right_frame.winfo_children():
        widget.destroy()
    
#SWITCHES TO PANIC WINDOW#
    if screen == "panic":
        Label(right_frame,
                text="EMERGENCY PANIC BUTTON",
                font=("Arial", 20, "bold"),
                bg=TEXT_COLOR).pack(pady=40)
        
        Button(right_frame,
                text="⚠️Activate Panic Button⚠️",
                command= windows.create_window,  
                font=("Arial", 14, "bold"),
                bg=BUTTON_COLOR,
                fg=BUTTON_TEXT_COLOR,
                height=2).place(x=235, y=250)
        
#SWITCHES TO DIFFERENT WINDOWS#
    elif screen == "instructions":
        Label(right_frame,
                text = "This is the emergency section\nClick a button to see the emergency instructions based on the category.",
                font = ("Arial", 15, "bold"),
                bg = TEXT_COLOR).pack(pady=40)
        
        #EMERGENCY INSTRUCTION IMAGES#
        Button(right_frame,
                text="Fire",
                command=windows.fire_create_window,
                font=("Arial", 14, "bold"),
                bg=BUTTON_COLOR,
                fg=BUTTON_TEXT_COLOR,
                width=25).place(x=220, y=150)
    
        Button(right_frame,
                text="Medical",
                command=windows.medical_create_window,
                font=("Arial", 14, "bold"),
                bg=BUTTON_COLOR,
                fg=BUTTON_TEXT_COLOR,
                width=25).place(x=220, y=210)
    
        Button(right_frame,
                text="Natural Disaster",
                command=windows.disaster_create_window,
                font=("Arial", 14, "bold"),
                bg=BUTTON_COLOR,
                fg=BUTTON_TEXT_COLOR,
                width=25).place(x=220, y=270)
                
#SWITCHES TO ADD HOTLINES WINDOW#
    elif screen == "add_hotlines":
        Label(right_frame,
            text="This is the add hotlines section",
            font=("Arial", 20, "bold"),
            bg=TEXT_COLOR).pack(pady=20)

        # ENTRY + BUTTON FIRST
        entry_row = Frame(right_frame, bg=WINDOW_COLOR)
        entry_row.pack(pady=10)

        entry = Entry(entry_row, font=("Arial", 20), width=20)
        entry.pack(side="left", padx=5)

        Button(entry_row,
            text="Add",
            font=("Arial", 14, "bold"),
            bg=BUTTON_COLOR,
            fg=BUTTON_TEXT_COLOR,
            command=lambda: add_hotline(entry)
            ).pack(side="left", padx=5)

        # THEN THE HOTLINES LIST UNDER IT
        try:
            with open("hotlineslist.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
        except FileNotFoundError:
            lines = []

        if not lines:
            Label(right_frame,
                text="No hotlines saved yet.",
                font=("Arial", 14),
                bg=WINDOW_COLOR).pack(pady=10)
        else:
            for hotline in lines:
                cleaned = hotline.strip()
                if not cleaned:
                    continue

                row = Frame(right_frame, bg=WINDOW_COLOR)
                row.pack(anchor="w", padx=50, pady=5, fill="x")

                Label(row,
                    text=cleaned,
                    font=("Arial", 14),
                    bg=WINDOW_COLOR,
                    fg=BUTTON_COLOR).pack(side="left")

                Button(row,
                    text="X",
                    font=("Arial", 12, "bold"),
                    fg=WINDOW_COLOR,
                    bg=BUTTON_COLOR,
                    command=lambda h=cleaned: delete_specific_hotline(h)
                    ).pack(side="left", padx=10) 
                
                Button(row,
                    text="Update",
                    font=("Arial", 12, "bold"),
                    fg=WINDOW_COLOR,
                    bg=BUTTON_COLOR,
                    command=lambda h=cleaned: open_update_window(h)
                    ).pack(side="left", padx=10)
                
    elif screen == "about":
        Label(right_frame,
                    text="Welcome to Protectly!\n\n"
                    "Protectly is an Emergency Safety App designed to help users quickly access "
                    "emergency panic buttons, instructions for fire, medical, and natural disaster "
                    "situations, and store important hotlines.\n\n"
                    "Stay safe and be prepared!",
                    font=("Arial", 14),
                    bg=WINDOW_COLOR,
                    justify="left",
                    wraplength=600).pack(pady=40, padx=20)
              
#-------------------------------------#

#WINDOW FOR PANIC BUTTON, SIZE, TITLE#
window = Tk()
window.geometry("1080x720")
window.title("Protectly")

#SIDEBAR#
sidebar = Frame(window,
            bg=SIDEBAR_COLOR,
            width=350)

sidebar.pack(side="left",
            fill="y"),
sidebar.pack_propagate(False)

#SIDEBAR NAME#
sidebar_name = Label(sidebar,
                text="Protectly: Emegency Safety App",
                bg=SIDEBAR_COLOR,
                fg=TEXT_COLOR,
                font=("Arial", 16, "bold"))
sidebar_name.pack(pady=30)

#SIDEBAR ROOF#
sidebar_roof = Frame(window,
                bg=SIDEBAR_COLOR,
                height=30)
sidebar_roof.pack(side="top",fill="x")

right_frame = Frame(window, bg=WINDOW_COLOR)
right_frame.pack(side="right", fill="both", expand=True)

#-------------------------------------#

#EMEGENCY PANIC BUTTON#
panic_button = Button(sidebar,
                text="Emergency Panic Button",
                font=("Sans-serif",14,"bold"),
                bg=BUTTON_COLOR,
                fg=BUTTON_TEXT_COLOR,
                command=lambda: show_content("panic"))
panic_button.pack(pady=20,padx=30,fill="x")

#INSTRUCTIONS BUTTON#
instructions_button = Button(sidebar,
                text="Emergency Instructions",
                font=("Sans-serif", 14, "bold"),
                bg=BUTTON_COLOR,
                fg=BUTTON_TEXT_COLOR,
                command=lambda: show_content("instructions"))
instructions_button.pack(pady=20,padx=30,fill="x")

#ADD HOTLINES BUTTON#
add_hotlines = Button(sidebar,
                text="Add Hotlines",
                font=("Sans-serif",14,"bold"),
                bg=BUTTON_COLOR,
                fg=BUTTON_TEXT_COLOR,
                command=lambda: show_content("add_hotlines"))
add_hotlines.pack(pady=20,padx=30,fill="x")

#ABOUT BUTTON#
about_button = Button(sidebar,
                text="About Protectly",
                font=("Sans-serif",14,"bold"),
                bg=BUTTON_COLOR,
                fg=BUTTON_TEXT_COLOR,
                command=lambda: show_content("about"))
about_button.pack(pady=20,padx=30,fill="x")

window.mainloop()