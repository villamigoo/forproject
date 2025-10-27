from tkinter import *
from tkinter import ttk

##################### Main Window #####################
window = Tk()
window.title("BSIT1-07 GROUP 3")
window.geometry("900x600")
window.configure(bg="#121212")

##################### MAIN FRAME #####################
main_frame = Frame(window, bg="#121212" )
main_frame.pack(fill='both', expand=True, padx=10, pady=10)

#####################    TITLE    #####################
Title = Label(
        main_frame,
        text="Face Recognition Based Attendance System",
        fg="white", bg="#262523",
        font=('Segoe UI', 20, 'bold'),
        pady=10
        )
Title.pack(fill='x')

##################### LEFT PANEL #####################
left = Frame(
        main_frame, 
        relief='ridge', 
        bd=2, bg="#1E1E1E",
        width=250
        )
left.pack(side='left', fill='y', padx=(0, 10))
left.pack_propagate(False) 

##################### RIGHT PANEL #####################
right = Frame(
        main_frame, 
        relief='ridge', 
        bd=2, 
        bg="#1E1E1E")
right.pack(side='left', fill='both', expand=True)
##################### LEFT: Controls #####################
left_frame_label = Label(
                        left, 
                        text="Student Registration", 
                        font=("Segoe UI", 18, "bold"), 
                        bg="#1E1E1E", 
                        fg="#FFFFFF")
left_frame_label.pack(pady=8)
#---------------------------------------------------------#
Label           (
                left, 
                text="Student ID:",
                bg="#1E1E1E", 
                fg="#FFFFFF", 
                font=("Arial", 13)
                ).pack(anchor='w', padx=8)

entry_id = Entry(
                left, 
                bg="#F5F5F5", 
                fg="black", 
                insertbackground="black", 
                font=("Segoe UI", 13)
                )
entry_id.pack(padx=8, pady=4)
#---------------------------------------------------------#
Label           (
                left, 
                text="Student Name:", 
                bg="#1E1E1E", 
                fg="#FFFFFF", 
                font=("Arial", 13)
                ).pack(anchor='w', padx=8)

entry_name = Entry(
                left, 
                bg="#F5F5F5", 
                fg="black", 
                insertbackground="black", 
                font=("Segoe UI", 13)
                )
entry_name.pack(padx=8, pady=4)
##################### BUTTON STYLE #####################
def enter(m):
    m.widget.config(bg="#3C3C3C")

def leave(m):
    m.widget.config(bg="#2D2D2D")

def student_btn_register(frame, text, fg_color, bg_color):
    button = Button(
        frame,
        text=text,
        width=20,
        fg = fg_color,
        bg = bg_color,
        activebackground="#3C3C3C",
        activeforeground="#FFFFFF",
        bd = 0,
        font = ("Segoe UI", 13, "bold")
    )

    button.bind("<Enter>", enter)
    button.bind("<Leave>", leave)

    return button


##################### BUTTON FOR STUDENT REGISTRATION #####################
student_btn_register(left, "Register Student", "#FF4C4C", "#2D2D2D").pack(pady=6)

Label   (
        left, 
        text="Capture & Model", 
        font=("Segoe UI", 12, "bold"), 
        bg="#1E1E1E", 
        fg="#FFFFFF").pack(pady=(12,4))

student_btn_register(left, "Take Images (Capture)", "#4287f5", "#2D2D2D").pack(pady=4)

student_btn_register(left, "Train Model", "#FFA500", "#2D2D2D").pack(pady=4)

student_btn_register(left, "Take Attendance", "#00C851", "#2D2D2D").pack(pady=8)

Label   (
        left, 
        text="Reports", 
        font=("Segoe UI", 12, "bold"), 
        bg="#1E1E1E", fg="#FFFFFF").pack(pady=(12,4))

student_btn_register(left,
"View Today's Attendance", "#000000", "#D9D9D9").pack(pady=4)

##################### RIGHT: Students & Messages #####################
right_top = Frame(right, bg="#1E1E1E")
right_top.pack(fill='x')

label_students = Label(
                    right_top, 
                    text="Registered Students", 
                    font=("Segoe UI", 14, "bold"), 
                    bg="#1E1E1E", 
                    fg="#FFFFFF")
label_students.pack(anchor='w', padx=6, pady=6)

style = ttk.Style()
style.theme_use("default")
style.configure("Treeview",
                background="#F5F5F5",
                foreground="black",
                rowheight=25,
                fieldbackground="#F5F5F5",
                font=("Segoe UI", 10))
style.configure("Treeview.Heading",
                background="#CCCCCC",
                foreground="black",
                font=('Segoe UI', 10, 'bold'))

tree_students = ttk.Treeview(right, columns=("name"), show='headings', height=12)
tree_students.heading('name', text='Name')
tree_students.column('name', width=300)
tree_students.pack(fill='x', padx=8)

##################### ATTENDANCE TABLE AREA #####################
right_bottom = Frame(right, bg="#1E1E1E")
right_bottom.pack(fill='both', expand=True, padx=50)