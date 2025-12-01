from tkinter import * 
from tkvideo import tkvideo
from playsound3 import playsound
import threading

def play_sound(window):
    threading.Thread(target=lambda: playsound("storage/image/emergecy_instructions/sound.mp3")).start()

def create_window():
    new_window = Toplevel()
    new_window.title("Panic Window")
    new_window.resizable(False, False)
    new_window.geometry(f"+{(new_window.winfo_screenwidth()-400)//2}+{(new_window.winfo_screenheight()-80)//2}")
    new_window.geometry("400x80")

    play_sound(new_window)
    
    label = Label(
                new_window,
                text="911 has been contacted!",
                font=('Arial', 12, 'bold'),
                fg="#b71c1c")
    label.place(x=110, y=25)

def fire_create_window():
    fire_window = Toplevel()
    fire_window.title("Fire Window")
    fire_window.geometry("800x770")
    fire_window.geometry(f"+{(fire_window.winfo_screenwidth()-800)//2}+{(fire_window.winfo_screenheight()-770)//2}")
    fire_window.resizable(False, False)
    video_label = Label(fire_window)
    video_label.pack()

    #PLAYS THE VIDEO# 
    player = tkvideo("storage/image/emergecy_instructions/Fire Emergency Instructions.mp4",
                     video_label,
                     loop=1,
                     size=(800, 500))
    player.play()

    title_label = Label(
        fire_window,
        text="FIRE EMERGENCY INSTRUCTIONS",
        font=("Arial", 16, "bold"),
        pady=10)
    title_label.pack()

    instructions = (
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

    text_label = Label(
    fire_window,
    text=instructions,
    font=("Arial", 14),
    padx=20,
    pady=10,
    anchor="w",
    justify="left")
    text_label.pack(fill="both", expand=True)

#OPENS MEDICAL INSTRUCTIONS#
def medical_create_window():
    medical_window = Toplevel()
    medical_window.title("Medical Window")
    medical_window.geometry("800x770")
    medical_window.geometry(f"+{(medical_window.winfo_screenwidth()-800)//2}+{(medical_window.winfo_screenheight()-770)//2}")
    medical_window.resizable(False, False)
    medical_video_label = Label(medical_window)
    medical_video_label.pack()

    #PLAYS THE VIDEO# 
    player = tkvideo("storage/image/emergecy_instructions/Medical Instructions.mp4",
                     medical_video_label,
                     loop=1,
                     size=(800, 500))
    player.play()

    title_label = Label(
        medical_window,
        text="MEDICAL EMERGENCY INSTRUCTIONS",
        font=("Arial", 16, "bold"),
        pady=10)
    title_label.pack()

    medical_instructions = (
        "1. Stay calm and assess the situation.\n"
        "2. Check if the person is conscious and breathing.\n"
        "3. If not breathing, call for help and start CPR if trained.\n"
        "4. Stop any heavy bleeding by applying pressure with a clean cloth.\n"
        "5. Do not move the injured person unless there’s danger nearby.\n"
        "6. Call emergency hotline 911 or the nearest hospital.\n"
        "7. If possible, note what happened and any symptoms.\n"
        "8. Stay with the person until help arrives."
    )

    text_label = Label(
    medical_window,
    text=medical_instructions,
    font=("Arial", 14),
    padx=20,
    pady=10,
    anchor="w",
    justify="left")
    text_label.pack(fill="both", expand=True)

def disaster_create_window():
    natural_window = Toplevel()
    natural_window.title("Natural Disaster Window")
    natural_window.geometry("800x770")
    natural_window.geometry(f"+{(natural_window.winfo_screenwidth()-800)//2}+{(natural_window.winfo_screenheight()-770)//2}")
    natural_window.resizable(False, False)
    natural_video_label = Label(natural_window)
    natural_video_label.pack()

    #PLAYS THE VIDEO# 
    player = tkvideo("storage/image/emergecy_instructions/Natural Disaster Instructions.mp4",
                     natural_video_label,
                     loop=1,
                     size=(800, 500))
    player.play()

    title_label = Label(
        natural_window,
        text="NATURAL DISASTER EMERGENCY INSTRUCTIONS",
        font=("Arial", 16, "bold"),
        pady=10)
    title_label.pack()

    disaster_instructions = (
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

    text_label = Label(
    natural_window,
    text=disaster_instructions,
    font=("Arial", 14),
    padx=20,
    pady=10,
    anchor="w",
    justify="left")
    text_label.pack(fill="both", expand=True)

def crime_security_create_window():
    crime_security_window = Toplevel()
    crime_security_window.title("Crime & Security")
    crime_security_window.geometry("800x770")
    crime_security_window.geometry(f"+{(crime_security_window.winfo_screenwidth()-800)//2}+{(crime_security_window.winfo_screenheight()-770)//2}")
    crime_security_window.resizable(False, False)
    crime_security_video_label = Label(crime_security_window)
    crime_security_video_label.pack()

    player = tkvideo("storage/image/emergecy_instructions/crime prevention.mp4",
                     crime_security_video_label,
                     loop=1,
                     size=(800, 500))
    player.play()

    title_label = Label(
        crime_security_window,
        text="CRIME & SECURITY EMERGENCY INSTRUCTIONS",
        font=("Arial", 16, "bold"),
        pady=10)
    title_label.pack()


    crime_security_instructions = (
        "1. Stay calm and avoid confrontation.\n"
        "2. Move to a safe and secure location immediately.\n"
        "3. Do NOT attempt to stop the suspect unless trained and necessary.\n"
        "4. Call emergency hotline 911 or local authorities right away.\n"
        "5. If possible, observe details: appearance, clothing, direction they went.\n"
        "6. Avoid touching or disturbing any evidence.\n"
        "7. If you are being followed, go to a public place and seek help.\n"
        "8. Lock doors and stay in a secure area until authorities arrive.\n"
        "9. Report everything clearly when help arrives."
    )

    text_label = Label(
    crime_security_window,
    text=crime_security_instructions,
    font=("Arial", 14),
    padx=20,
    pady=10,
    anchor="w",
    justify="left")
    text_label.pack(fill="both", expand=True)


def chemical_create_window():
    chemical_window = Toplevel()
    chemical_window.title("Chemical / Hazardous Materials")
    chemical_window.geometry("800x770")
    chemical_window.geometry(f"+{(chemical_window.winfo_screenwidth()-800)//2}+{(chemical_window.winfo_screenheight()-770)//2}")
    chemical_window.resizable(False, False)
    chemical_video_label = Label(chemical_window)
    chemical_video_label.pack()

    player = tkvideo("storage/image/emergecy_instructions/Chemical hazards.mp4",
                     chemical_video_label,
                     loop=1,
                     size=(800, 500))
    player.play()

    title_label = Label(
        chemical_window,
        text="CHEMICAL / HAZAROUS EMERGENCY INSTRUCTIONS",
        font=("Arial", 16, "bold"),
        pady=10)
    title_label.pack()

    chemical_instructions = (
        "1. Stay calm — do NOT inhale or touch any substances.\n"
        "2. Immediately move away from the affected area.\n"
        "3. Cover your nose and mouth with a cloth or mask if fumes are present.\n"
        "4. Avoid using electrical switches or flames near chemicals.\n"
        "5. Call emergency hotline 911 or hazardous materials team.\n"
        "6. If exposed, wash skin with clean water for at least 15 minutes.\n"
        "7. Remove contaminated clothing carefully.\n"
        "8. Do NOT attempt to clean spills without proper training.\n"
        "9. Wait for professionals and report what happened clearly."
    )

    text_label = Label(
    chemical_window,
    text=chemical_instructions,
    font=("Arial", 14),
    padx=20,
    pady=10,
    anchor="w",
    justify="left")
    text_label.pack(fill="both", expand=True)

def transportation_create_window():
    transportation_window = Toplevel()
    transportation_window.title("Transportation")
    transportation_window.geometry("800x770")
    transportation_window.geometry(f"+{(transportation_window.winfo_screenwidth()-800)//2}+{(transportation_window.winfo_screenheight()-770)//2}")
    transportation_window.resizable(False, False)
    transportation_video_label = Label(transportation_window)
    transportation_video_label.pack()

    player = tkvideo("storage/image/emergecy_instructions/transportation.mp4",
                     transportation_video_label,
                     loop=1,
                     size=(800, 500))
    player.play()

    title_label = Label(
        transportation_window,
        text="TRANSPORTATION EMERGENCY INSTRUCTIONS",
        font=("Arial", 16, "bold"),
        pady=10)
    title_label.pack()

    transportation_instructions = (
        "1. Stay calm and check for injuries.\n"
        "2. Do NOT move injured persons unless there is danger (fire, explosion, etc.).\n"
        "3. Call emergency hotline 911 immediately.\n"
        "4. If safe, turn on hazard lights to warn other vehicles.\n"
        "5. Move to a safe area away from traffic if possible.\n"
        "6. Apply first aid only if trained to do so.\n"
        "7. Document details (location, injuries, what happened).\n"
        "8. Wait for emergency responders and follow their instructions.\n"
        "9. Stay alert for traffic or secondary accidents."
    )

    text_label = Label(
    transportation_window,
    text=transportation_instructions,
    font=("Arial", 14),
    padx=20,
    pady=10,
    anchor="w",
    justify="left")
    text_label.pack(fill="both", expand=True)