from tkinter import *
from tkinter import messagebox
from message_scanner import scan_message
from url_checker import scan_url
from number_checker import scan_number
import pygame
import time
pygame.init()
pygame.init()
def music(stage):
    musics = {

        "geet": "ROLEX.mp3",
        "feet": "LEO.mp3",
        
    }
    if stage in musics:
        pygame.mixer.music.load(musics[stage])
        pygame.mixer.music.play()
        print(f"🔊 Playing {stage.upper()} music...\n")
        time.sleep(2)  # wait for music to start


def fraud_message():
    write = message_detect.get().strip()
    if write == "":
        messagebox.showerror("PROBLEM", "BRO WHAT THE HELL IS GOING WRONG WITH YOU")
    else: 
        music("geet")
        messagebox.showinfo("Scan Result", f"Bhai message scan ho gaya! 😎\nMessage: {write}")
        messagebox.showwarning("SCANNED MESSAGE",scan_message(write))
       


def fraud_link(event=None):
    likh = scanurl.get().strip()
    if likh == "":
        messagebox.showwarning("URL Scan", "Bhai URL likh to sahi!")
    else:
        music("feet")
        messagebox.showinfo("URL Scan", f"URL scanned successfully: {likh}")
        messagebox.showwarning("SCANNED URL",scan_url(likh))
        

def fraud_num():
   f=num.get().strip()

   if f=="":
       messagebox.showerror("ERROR ERROR","HELL WHAT THE CRAZY SHIT YOU DONE!!!")
   else:
       messagebox.showinfo("number scanned",f"number scan hogaya: {f}")
       messagebox.showwarning("SCANNED NUMBER",scan_number(f))
       music("geet")
       

# Window Setup
window = Tk()
window.title("DANUJ CYBERSHIELD")
window.geometry("500x350")  # Initial size
window.minsize(400, 300)
window.config(bg="#1E1E1E")

# Configure grid weights for responsiveness
window.columnconfigure(0, weight=1)
window.rowconfigure([0, 1, 2, 3, 4], weight=1)

# Title Label
sc = Label(
    window,
    text="SCAN THE FUCKING MESSAGE!!!",
    background="#00ff00",
    font=("Arial", 14, "bold"),
    wraplength=400
)
sc.grid(row=0, column=0, pady=10, sticky="nsew")

# Message Entry
message_detect = Entry(
    window,
    font=("Ink Free", 15, "bold"),
    fg="white",
    bg="#1E1E1E",
    insertbackground="white"
)
message_detect.grid(row=1, column=0, pady=10, padx=20, sticky="nsew")

# Message Scan Button
mebut = Button(
    window,
    text="SCAN THE MESSAGE MAN!!!",
    font=("Arial", 12, "bold"),
    background="#BDB76B",
    fg="#191970",
    command=fraud_message
)
mebut.grid(row=2, column=0, pady=10, padx=20, sticky="nsew")

# URL Entry

ur=Label(window,text="WRITE THE FUCKING LINK DOWN BELOW👇👇!!!!",font=("arial",12,"bold")).grid(row=3,column=0,padx=20,pady=10,sticky="nsew")
scanurl = Entry(
    window,
    font=("Arial", 12),
    background="#E6E6FA"
)
scanurl.grid(row=4, column=0, pady=10, padx=20, sticky="nsew")
scanurl.bind("<Return>", fraud_link)

# Number Entry

r=Label(window,text="WRITE THE FUCKING NUMBER DOWN BELOW👇👇!!!!",font=("arial",12,"bold")).grid(row=5,column=0,padx=20,pady=10,sticky="nsew")
num = Entry(
    window,
    font=("Ink Free", 13),
    fg="red"
)
num.grid(row=6, column=0, pady=10, padx=20, sticky="nsew")

numbut=Button(window,text="PUSH THE DAMN BUTTON!!!!",font=("JAVANESE"),command=fraud_num).grid(row=7,column=0)
window.mainloop()
