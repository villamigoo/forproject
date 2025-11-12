from tkinter import * 
from PIL import Image, ImageTk

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

def fire_create_window():
    fire_window = Toplevel()
    fire_window.title("Fire Window")
    fire_window.geometry("600x720")

    fire_image = Image.open("fire_emergency.png")
    fire_photo = ImageTk.PhotoImage(fire_image)
    label = Label(fire_window, 
                image=fire_photo,
                compound="top",
                font=("Arial",12,"bold"))
    label.image = fire_photo
    label.pack()

    instructions = (
        " FIRE EMERGENCY INSTRUCTIONS \n\n"
        "1. Stay calm — do not panic.\n"
        "2. Activate the nearest fire alarm.\n"
        "3. Evacuate the building immediately using the stairs.\n"
        "4. Do NOT use elevators.\n"
        "5. If theres smoke, stay low and cover your mouth with a cloth.\n"
        "6. Help others if its safe to do so.\n"
        "7. Once outside, move to the designated safe area.\n"
        "8. Call emergency hotline 911 or the local fire department.\n"
        "9. Do not return until authorities say its safe."
    )

    text_label = Label(fire_window,
                       text=instructions,
                       font=("Arial", 12),
                       padx=20,
                       pady=10)
    text_label.pack()

#OPENS MEDICAL INSTRUCTIONS#
def medical_create_window():
    medical_window = Toplevel()
    medical_window.title("Medical")
    medical_window.geometry("600x720")

    medical_image = Image.open("medical_emergencyy.png")
    medical_photo = ImageTk.PhotoImage(medical_image)
    label = Label(medical_window,
                  image=medical_photo,
                  compound="top",
                  font=("Arial",12,"bold"))
    label.image = medical_photo
    label.pack()

    medical_instructions = (
        " MEDICAL EMERGENCY INSTRUCTIONS \n\n"
        "1. Stay calm and assess the situation.\n"
        "2. Check if the person is conscious and breathing.\n"
        "3. If not breathing, call for help and start CPR if trained.\n"
        "4. Stop any heavy bleeding by applying pressure with a clean cloth.\n"
        "5. Do not move the injured person unless there’s danger nearby.\n"
        "6. Call emergency hotline 911 or the nearest hospital.\n"
        "7. If possible, note what happened and any symptoms.\n"
        "8. Stay with the person until help arrives."
    )

    text_label = Label(medical_window,
                       text=medical_instructions,
                       font=("Arial", 12),
                       padx=20,
                       pady=10)
    text_label.pack()

def disaster_create_window():
    disaster_window = Toplevel()
    disaster_window.title("Disaster")
    disaster_window.geometry("600x720")
   
    image = Image.open("natural_disaster.png")  
    photo = ImageTk.PhotoImage(image)
    label = Label(disaster_window,
                  image=photo,
                  compound="top",  
                  font=("Arial", 12, "bold"))
    label.image = photo
    label.pack()

    disaster_instructions = (
        " NATURAL DISASTER INSTRUCTIONS \n\n"
        "1. Stay calm and listen to official announcements.\n"
        "2. If indoors, move away from windows and heavy furniture.\n"
        "3. Take cover under a sturdy table or desk during earthquakes.\n"
        "4. If outdoors, go to an open area away from buildings and trees.\n"
        "5. Prepare an emergency kit (water, flashlight, first aid, radio).\n"
        "6. Follow evacuation orders if instructed by authorities.\n"
        "7. Avoid using elevators during disasters.\n"
        "8. Stay tuned to local radio or news for updates.\n"
        "9. Help others and stay alert for aftershocks or secondary hazards."
    )

    text_label = Label(disaster_window,
                       text=disaster_instructions,
                       font=("Arial", 12),
                       padx=20,
                       pady=10)
    text_label.pack()