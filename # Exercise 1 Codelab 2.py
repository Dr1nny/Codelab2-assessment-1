# Exercise 1 Codelab 2
from tkinter import *
import random
from tkinter import messagebox

hearts = 5 #the ammount of tries before the user runs out of attempts
questions_for_quiz = 10 # how many questions will there be for each difficulty

def displayMenu():
    menu=Toplevel(root)
    menu.title("Difficulty")
    menu.geometry("800x500")
    menu.config(bg="#22628e")

    Label(menu, text="Choose your difficulty", font=("Tahoma", 24, "bold"), bg="#22628e", fg="white").pack(pady=20)

    Button(menu, text="Easy", font=("Tahoma", 20, "bold"), bg="#22628e", width=15).pack(pady=20)
    Button(menu, text="Medium", font=("Tahoma", 20, "bold"), bg="#22628e", width=15).pack(pady=20)
    Button(menu, text="Hard", font=("Tahoma", 20, "bold"), bg="#22628e", width=15).pack(pady=20)

    Button(menu, text="Go Back", font=("Tahoma", 20, "bold"), bg="#22628e", width=5, command=lambda:back_menu(menu)).pack(pady=20)

def back_menu(menu):
    go_back = messagebox.askyesno("Confirm","Do you want to go back to the menu?")
    if go_back:
        menu.destroy()


def destroy():
    answer = messagebox.askyesno("Exit", "Would you like to close the app?")
    if answer:
        root.destroy()


#Set output window
root=Tk()
root.title("Test your Math!")
root.geometry("800x500")
root.config(bg="#22628e")

#Create a label to describe and interact with environment using buttons that takes user to the math quiz
titletext = Label(root, text="Math Quiz!" ,font=("Tahoma",30,"bold"),bg="#22628e", pady=10).pack()

description = Label(root, text="Test your math skills now!", font=("Tahoma",24,"bold"), bg="#22628e")
description.place(x=175, y=100)

bt1 = Button(root, text="Play Now", font=("Tahoma", 20, "bold"), bg="#22628e", command=displayMenu)
bt1.place(x=317, y=150)

e1 = Button(root, text = "Exit", fg="Black", bg="#001111",font=("tahoma",12, "bold"),command = destroy)
e1.place(x=173,y=350)

#Buttons that opens a window for difficulty modes



root.mainloop()