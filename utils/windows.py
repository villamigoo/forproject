from tkinter import * 
from PIL import Image, ImageTk
from tkvideo import tkvideo

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
    fire_window.geometry("800x750")
    video_label = Label(fire_window)
    video_label.pack()

    #PLAYS THE VIDEO# 
    player = tkvideo("storage/image/emergecy_instructions/Fire Emergency Instructions.mp4",
                     video_label,
                     loop=1,
                     size=(800, 500))
    player.play()

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
    medical_window.title("Fire Window")
    medical_window.geometry("800x750")
    medical_video_label = Label(medical_window)
    medical_video_label.pack()

    #PLAYS THE VIDEO# 
    player = tkvideo("storage/image/emergecy_instructions/Medical Instructions.mp4",
                     medical_video_label,
                     loop=1,
                     size=(800, 500))
    player.play()

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
    natural_window = Toplevel()
    natural_window.title("Fire Window")
    natural_window.geometry("800x750")
    natural_video_label = Label(natural_window)
    natural_video_label.pack()

    #PLAYS THE VIDEO# 
    player = tkvideo("storage/image/emergecy_instructions/Natural Disaster Instructions.mp4",
                     natural_video_label,
                     loop=1,
                     size=(800, 500))
    player.play()

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

    text_label = Label(natural_window,
                       text=disaster_instructions,
                       font=("Arial", 12),
                       padx=20,
                       pady=10)
    text_label.pack()