from tkinter import *

# ----- COLOR VARIABLES -----
SIDEBAR_COLOR = "blue"        # sidebar background
SIDEBAR_TEXT_COLOR = "white"     # sidebar text
RIGHT_BG = "purple"             # right frame background
BUTTON_BG = "orange"            # buttons background
BUTTON_FG = "white"              # buttons text
POPUP_BG = "green"             # popup window background
POPUP_TEXT_COLOR = "#000000"     # popup text color

# ----- FUNCTION TO CREATE POPUP -----
def show_popup(title, message):
    popup = Toplevel()
    popup.title(title)
    popup.geometry("400x200")
    popup.configure(bg=POPUP_BG)
    
    Label(popup, text=message, font=("Arial", 14, "bold"), bg=POPUP_BG, fg=POPUP_TEXT_COLOR).pack(pady=40)
    
    Button(popup, text="Close", bg=BUTTON_BG, fg=BUTTON_FG, command=popup.destroy).pack(pady=20)

# ----- FUNCTION TO SHOW CONTENT -----
def show_content(screen):
    for widget in right_frame.winfo_children():
        widget.destroy()

    if screen == "panic":
        Label(right_frame,
              text="Emergency panic button",
              font=("Arial", 20, "bold"),
              bg=RIGHT_BG).pack(pady=40)
        
        Button(right_frame,
               text="⚠️Activate Panic Button⚠️",
               font=("Arial", 14, "bold"),
               bg=BUTTON_BG,
               fg=BUTTON_FG,
               height=2,
               command=lambda: show_popup("Panic Activated", "Emergency Panic Button Activated!")
               ).pack(pady=20)

    elif screen == "instructions":
        Label(right_frame,
              text="This is the emergency instructions section",
              font=("Arial", 15, "bold"),
              bg=RIGHT_BG).pack(pady=40)

        Button(right_frame,
               text="Fire",
               font=("Arial", 14, "bold"),
               bg=BUTTON_BG,
               fg=BUTTON_FG,
               command=lambda: show_popup("Fire Instructions", "Follow fire safety procedures!")
               ).pack(pady=10)

        Button(right_frame,
               text="Medical",
               font=("Arial", 14, "bold"),
               bg=BUTTON_BG,
               fg=BUTTON_FG,
               command=lambda: show_popup("Medical Instructions", "Call medical help immediately!")
               ).pack(pady=10)

        Button(right_frame,
               text="Natural Disaster",
               font=("Arial", 14, "bold"),
               bg=BUTTON_BG,
               fg=BUTTON_FG,
               command=lambda: show_popup("Disaster Instructions", "Follow disaster safety protocols!")
               ).pack(pady=10)

    elif screen == "hotlines":
        Label(right_frame,
              text="Hotlines List",
              font=("Arial", 20, "bold"),
              bg=RIGHT_BG).pack(pady=20)

        hotlines = ["Police: 911", "Fire: 911", "Medical: 911"]
        for hotline in hotlines:
            Button(right_frame,
                   text=hotline,
                   bg=BUTTON_BG,
                   fg=BUTTON_FG,
                   command=lambda h=hotline: show_popup("Hotline", h)
                   ).pack(pady=5, padx=50, fill="x")

    elif screen == "add_hotlines":
        Label(right_frame,
              text="Add Hotlines Section",
              font=("Arial", 20, "bold"),
              bg=RIGHT_BG).pack(pady=40)

        Button(right_frame,
               text="Add Sample Hotline",
               bg=BUTTON_BG,
               fg=BUTTON_FG,
               command=lambda: show_popup("Add Hotline", "Practice adding a hotline!")).pack(pady=10)

    elif screen == "about":
        Label(right_frame,
              text="About Protectly",
              font=("Arial", 20, "bold"),
              bg=RIGHT_BG).pack(pady=40)

        Button(right_frame,
               text="About App",
               bg=BUTTON_BG,
               fg=BUTTON_FG,
               command=lambda: show_popup("About Protectly", "This is a demo emergency safety app.")).pack(pady=10)

# ----- MAIN WINDOW -----
window = Tk()
window.geometry("1080x720")
window.title("Protectly")

# ----- SIDEBAR -----
sidebar = Frame(window, bg=SIDEBAR_COLOR, width=350)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

Label(sidebar, text="Protectly: Emergency Safety App",
      bg=SIDEBAR_COLOR, fg=SIDEBAR_TEXT_COLOR,
      font=("Arial", 16, "bold")).pack(pady=30)

# Sidebar Buttons
buttons_info = [
    ("Emergency Panic Button", "panic"),
    ("Emergency Instructions", "instructions"),
    ("Hotlines List", "hotlines"),
    ("Add Hotlines", "add_hotlines"),
    ("About Protectly", "about")
]

for text, screen_name in buttons_info:
    Button(sidebar,
           text=text,
           font=("Sans-serif", 14, "bold"),
           bg=BUTTON_BG,
           fg=BUTTON_FG,
           command=lambda s=screen_name: show_content(s)
           ).pack(pady=20, padx=30, fill="x")

# ----- RIGHT FRAME -----
right_frame = Frame(window, bg=RIGHT_BG)
right_frame.pack(side="right", fill="both", expand=True)

window.mainloop()