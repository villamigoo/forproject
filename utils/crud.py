from tkinter import messagebox, Toplevel, Label, Entry, Button
from tkinter import END
import re

#COPY HOTLINE NUMBER#
def copy_hotline_to_clipboard(window, text):
    number = "".join(re.findall(r"\d+", text))
    window.clipboard_clear()
    window.clipboard_append(number)
    messagebox.showinfo("Copied", "Hotline number copied!")

#WINDOW FOR CALL HOTLINE#
def call_hotline_window(hotline_number):
    call_win = Toplevel()
    call_win.title("Call Hotline")
    call_win.geometry("350x150")
    call_win.geometry(f"+{(call_win.winfo_screenwidth()-350)//2}+{(call_win.winfo_screenheight()-150)//2}")
    call_win.resizable(False, False)

    Label(call_win, text="Enter number to call:", font=("Arial", 14)).pack(pady=(20,5))

    number_entry = Entry(call_win, font=("Arial", 14), width=20)
    number_entry.pack(pady=5)
    number_entry.insert(0, hotline_number)

    def start_call():
        number = number_entry.get().strip()
        if not number.isdigit():
            messagebox.showerror("Invalid Input", "Please enter numbers only!")
            return
        messagebox.showinfo("Calling...", f"Calling {number}...")
        call_win.destroy()

    Button(call_win, text="Call", font=("Arial", 12, "bold"), bg="green", fg="white",
           command=start_call).pack(pady=10)

#ADDS THE TYPED NUMBER TO THE HOTLINES LIST WINDOW"
def add_hotline(entry, show_content):
    hotline = entry.get().strip()

    if not re.fullmatch(r"[A-Za-z][A-Za-z .,&()-]{3,}\s*-\s*[\d ()-]{3,}", hotline):
        messagebox.showerror(
            "Invalid Input", 
            "Please enter in this format: Name (letters only) followed by number (at least 3 digits)."
        )
        return
   
   #CHECKS IF NUMBER IS ALREADY IN HOTLINES LIST#
    number_part = "".join(re.findall(r"\d+", hotline.split("-", 1)[1]))
    existing = { "".join(re.findall(r"\d+", line.split("-", 1)[1])) for line in open("hotlineslist.txt", encoding="utf-8") }

    if number_part in existing:
        messagebox.showerror("Duplicate Hotline", f"The number {number_part} already exists!")
        return

    # AVE IF NO DUPLICATE#
    with open("hotlineslist.txt", "a", encoding="utf-8") as file:
        file.write(hotline + "\n")
  
    messagebox.showinfo("Success", "Hotline added successfully!")

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

#OPENS WINDOW FOR UPDATING HOTLINES#
def open_update_window(old_value, show_content, BUTTON_COLOR, WINDOW_COLOR):
    update_win = Toplevel()
    update_win.title("Update Hotline")
    update_win.geometry("400x200")
    update_win.geometry(f"+{(update_win.winfo_screenwidth()-400)//2}+{(update_win.winfo_screenheight()-200)//2}")

    Label(update_win, text="Update Hotline:", font=("Arial", 14)).pack(pady=10)

    entry = Entry(update_win, font=("Arial", 14), width=25)
    entry.pack(pady=5)
    entry.insert(0, old_value)

    def save_update():
        new_value = entry.get().strip()
        if new_value:
            update_hotline(old_value, new_value)
            messagebox.showinfo("Success", "Hotline updated successfully!")
            show_content("add_hotlines")
            update_win.destroy()

    Button(update_win,
           text="Save",
           font=("Arial", 12, "bold"),
           bg=BUTTON_COLOR,
           fg=WINDOW_COLOR,
           command=save_update).pack(pady=10)

#DELETES HOTLINE#
def delete_specific_hotline(hotline, show_content):
    with open("hotlineslist.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open("hotlineslist.txt", "w", encoding="utf-8") as file:
        for line in lines:
            if line.strip() != hotline:
                file.write(line)

    messagebox.showinfo("Success", "Hotline deleted successfully!")    
    show_content("add_hotlines")