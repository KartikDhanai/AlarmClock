from tkinter import *
from datetime import datetime
import pygame

pygame.mixer.init()

# Function to play music
def play_music():
    pygame.mixer.music.load("alarm_sound.mp3")
    pygame.mixer.music.play()

# Function to set the alarm
def set_alarm():
    current_time = datetime.now().strftime("%I:%M:%S %p")
    
    alarm_time = entry.get()
    
    # Check if alarm time is valid
    try:
        datetime.strptime(alarm_time, "%I:%M:%S %p")
    except ValueError:
        label.config(text="Invalid time format!", fg="red")
        return
    
    # Calculate time until alarm
    time_until_alarm = (datetime.strptime(alarm_time, "%I:%M:%S %p") - datetime.strptime(current_time, "%I:%M:%S %p")).total_seconds()
    
    # Set timer to play music when alarm goes off
    root.after(int(time_until_alarm * 1000), play_music)
    
    # Update label to show alarm is set
    label.config(text=f"Alarm set for {alarm_time}.", fg="green")

# Create GUI window
root = Tk()
root.title("Alarm Clock")
root.geometry("1010x650")

bg_image = PhotoImage(file="ALARM CLOCK.png")
bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

label = Label(root, text="Enter alarm time (HH:MM:SS AM/PM):", font=("Arial", 20), bg="#FFFFCC")
label.grid(row=0, column=0, padx=50, pady=70)

entry = Entry(root, font=("Arial", 30), width=15)
entry.grid(row=0, column=1, padx=10, pady=10)

button = Button(root, text="Set Alarm", font=("Arial", 20), bg="#CDCD91", command=set_alarm)
button.grid(row=1, column=0, columnspan=2, padx=50, pady=70)

root.mainloop()
