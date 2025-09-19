from tkinter import *
import tkinter as tk

from analyseur import *

def synth():
    print(page.extract_text())


window = tk.Tk()

window.config(bg="white", bd=0)
window.geometry(("800x600"))

frame = Frame(window, bg="white", bd=0)

label = Label(frame, text="Enter the path where your doc is\n | \n\/", bg="white")
label.pack()

entry = Entry(frame, text="", bg="white")
entry.pack()

generate = Button(frame, text="Generate Doc", bg="white", command=synth)
generate.pack()


frame.pack(expand=YES)

window.mainloop()