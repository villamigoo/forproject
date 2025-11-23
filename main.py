from tkinter import *
from utils import windows
from utils import crud
from tkinter import PhotoImage

#COLORS#
SIDEBAR_COLOR = "dark red"
BUTTON_COLOR = "dark red"
HOME_TEXT_COLOR = "black"
PANIC_BUTTON_TEXT = "red"
UPDATE_BUTTON_COLOR = "green"
BUTTON_TEXT_COLOR = "white"
TITLE_TEXT_COLOR = "black"
TEXT_COLOR = "white"
WINDOW_COLOR ="white"

active_button = None

#SUNKEN BUTTON FEEL#
def set_active(btn):
        global active_button
        if active_button:  
            active_button.config(relief="raised", bg=BUTTON_COLOR)
        btn.config(relief="sunken") 
        active_button = btn

#ADDS THE TYPED NUMBER TO THE HOTLINES LIST WINDOW"
def add_hotline(entry):
    hotline = entry.get().strip()
    if hotline:
        with open("hotlineslist.txt", "a", encoding="utf-8") as file:
            file.write(hotline + "\n")
        entry.delete(0, END)
    show_content("add_hotlines")

#UPDATES HOTLINE#
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

#DELETES HOTLINE#
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
    
#DISPLAYS PROTECTLY TITLE#
    if screen == "home":
        Label(right_frame,
                text="Welcome to Protectly!",
                font=("Arial", 40, "bold"),
                bg=WINDOW_COLOR,
                fg=TITLE_TEXT_COLOR).place(x=90, y=30)
        
        logo_raw = PhotoImage(file="storage/image/emergecy_instructions/app logo.png")
        logo_image = logo_raw

        logo_canvas = Canvas(right_frame,
                            width=350,
                            height=300,
                            bg=WINDOW_COLOR,
                            highlightthickness=0)
        logo_canvas.place(x=190, y=150)
        logo_canvas.create_image(175, 150, image=logo_image) 
        logo_canvas.image = logo_image

        Label(right_frame,
        text="Your safety, one click away.\nStay calm, stay prepared, and Protectly will guide you.",
        font=("Arial", 16, "italic"),
        bg=WINDOW_COLOR,
        fg=HOME_TEXT_COLOR).pack(pady=(500, 50))
    

#SWITCHES TO PANIC BUTTON#
    elif screen == "panic":
        Label(right_frame,
                text="EMERGENCY PANIC BUTTON",
                font=("Arial", 20, "bold"),
                bg=TEXT_COLOR).pack(pady=40)
        
        Label(right_frame,
                text="Instructions: In case of danger, press the button below.\n"
                     "It will instantly send an alert to your hotline contacts.\n"
                     "so they can respond to the emergency as fast as possible.",
                font=("Arial", 14, "bold"),
                bg=TEXT_COLOR,
                fg=PANIC_BUTTON_TEXT).pack(pady=5)
        
        Label(right_frame,
                text="Important notice: Only press the button when in an emergency",
                font=("Arial", 14, "bold"),
                bg=TEXT_COLOR,
                fg=PANIC_BUTTON_TEXT).pack(pady=5)
              
        
        Button(right_frame,
                text="⚠️Activate Panic Button⚠️",
                command= windows.create_window,  
                font=("Arial", 14, "bold"),
                bg=BUTTON_COLOR,
                fg=BUTTON_TEXT_COLOR,
                height=2).place(x=235, y=300)
        
#SWITCHES TO DIFFERENT WINDOWS#
    elif screen == "instructions":
        Label(right_frame,
                text = "Emergency Instructions section\nClick a button to see the emergency instructions based on the category.",
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
        
        Button(right_frame,
               text="Crime & Security",
               command=windows.crime_security_create_window,
               font=("Arial", 14, "bold"),
               bg=BUTTON_COLOR,
               fg=BUTTON_TEXT_COLOR,
               width=25).place(x=220, y=330)
        
        Button(right_frame,
               text="Chemical / Hazardous Materials",
               command=windows.chemical_create_window,
               font=("Arial", 14, "bold"),
               bg=BUTTON_COLOR,
               fg=BUTTON_TEXT_COLOR,
               width=25).place(x=220, y=390)

        Button(right_frame,
               text="Transportation",
               command=windows.transportation_create_window,
               font=("Arial", 14, "bold"),
               bg=BUTTON_COLOR,
               fg=BUTTON_TEXT_COLOR,
               width=25).place(x=220, y=450)
               
#SWITCHES TO ADD HOTLINES WINDOW#
    elif screen == "add_hotlines":
        Label(right_frame,
            text="Add hotlines section",
            font=("Arial", 20, "bold"),
            bg=TEXT_COLOR).pack(pady=20)

        entry_row = Frame(right_frame, bg=WINDOW_COLOR)
        entry_row.pack(pady=10)

        entry = Entry(entry_row, font=("Arial", 20), width=20)
        entry.pack(side="left", padx=5)

        Button(entry_row,
            text="Add",
            font=("Arial", 14, "bold"),
            bg=BUTTON_COLOR,
            fg=BUTTON_TEXT_COLOR,
            width=5,
            command=lambda: add_hotline(entry)
            ).pack(side="left", padx=5)

        list_frame = Frame(right_frame, bg=WINDOW_COLOR)
        list_frame.pack(pady=10, anchor="w", padx=30)

        try:
            with open("hotlineslist.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
        except FileNotFoundError:
            lines = []

        if not lines:
            Label(list_frame,
                text="No hotlines saved yet.",
                font=("Arial", 14),
                bg=WINDOW_COLOR).grid(row=0, column=0, pady=10)
        else:
            for i, hotline in enumerate(lines):
                cleaned = hotline.strip()
                if not cleaned:
                    continue

                Label(list_frame,
                    text=cleaned,
                    font=("Arial", 14),
                    bg=WINDOW_COLOR,
                    fg=BUTTON_COLOR,
                    anchor="w",
                    width=35).grid(row=i, column=0, sticky="w", padx=5, pady=5)

                Button(list_frame,
                    text="Delete",
                    font=("Arial", 12, "bold"),
                    fg=WINDOW_COLOR,
                    bg=BUTTON_COLOR,
                    width=10,
                    command=lambda h=cleaned: delete_specific_hotline(h)
                    ).grid(row=i, column=1, padx=5, pady=5)

                Button(list_frame,
                    text="Update",
                    font=("Arial", 12, "bold"),
                    fg=WINDOW_COLOR,
                    bg=UPDATE_BUTTON_COLOR,
                    width=10,
                    command=lambda h=cleaned: open_update_window(h)
                    ).grid(row=i, column=2, padx=5, pady=5)
                
    elif screen == "about":
        Label(right_frame,
                    text="Welcome to Protectly!\n\n"
                    "Protectly is an Emergency Safety App designed to help users quickly access "
                    "emergency panic buttons, instructions for fire, medical, natural disasters, "
                    "crime & security, chemicals, and transportation situations and store important hotlines.\n\n"
                    "Stay safe and be prepared!",
                    font=("Arial", 14),
                    bg=WINDOW_COLOR,
                    justify="left",
                    wraplength=600).pack(pady=40, padx=20)
              
#-------------------------------------#

#WINDOW FOR PANIC BUTTON, SIZE, TITLE#
window = Tk()
window.geometry("1080x720")
window.geometry(f"+{(window.winfo_screenwidth()-1080)//2}+{(window.winfo_screenheight()-720)//2}")
window.title("Protectly")
window.resizable(False, False)
window.attributes('-toolwindow', True)

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


logo_raw = PhotoImage(file="storage/image/emergecy_instructions/app logo.png")
logo_image = logo_raw

logo_canvas = Canvas(sidebar,
                     width=350,
                     height=300,
                     bg=SIDEBAR_COLOR,
                     highlightthickness=0)
logo_canvas.pack(pady=(10, 20))
logo_canvas.create_image(175, 150, image=logo_image) 
logo_canvas.image = logo_image

right_frame = Frame(window, bg=WINDOW_COLOR)
right_frame.pack(side="right", fill="both", expand=True)

#-------------------------------------#

button_frame = Frame(sidebar, bg=SIDEBAR_COLOR)
button_frame.pack(side="bottom", fill="x", pady=20)

#EMEGENCY PANIC BUTTON#
panic_button = Button(button_frame,
                text="🆘 Emergency Panic Button",
                font=("Sans-serif",14,"bold"),
                bg=BUTTON_COLOR,
                fg=BUTTON_TEXT_COLOR,
                anchor="w",
                padx=10,
                command=lambda: [show_content("panic"), set_active(panic_button)])
panic_button.pack(pady=10,padx=30,fill="x")

#INSTRUCTIONS BUTTON#
instructions_button = Button(button_frame,
                text="⚠️ Emergency Instructions",
                font=("Sans-serif", 14, "bold"),
                bg=BUTTON_COLOR,
                fg=BUTTON_TEXT_COLOR,
                anchor="w",
                padx=10,
                command=lambda: [show_content("instructions"), set_active(instructions_button)])
instructions_button.pack(pady=10,padx=30,fill="x")

#ADD HOTLINES BUTTON#
add_hotlines = Button(button_frame,
                text="📞 Add Hotlines",
                font=("Sans-serif",14,"bold"),
                bg=BUTTON_COLOR,
                fg=BUTTON_TEXT_COLOR,
                anchor="w",
                padx=10,
                command=lambda: [show_content("add_hotlines"), set_active(add_hotlines)])
add_hotlines.pack(pady=10,padx=30,fill="x")

#ABOUT BUTTON#
about_button = Button(button_frame,
                text="❗ About Protectly",
                font=("Sans-serif",14,"bold"),
                bg=BUTTON_COLOR,
                fg=BUTTON_TEXT_COLOR,
                anchor="w",
                padx=10,
                command=lambda: [show_content("about"), set_active(about_button)])
about_button.pack(pady=10,padx=30,fill="x")

show_content("home")

window.mainloop()