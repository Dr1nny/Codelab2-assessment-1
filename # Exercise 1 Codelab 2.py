# Exercise 1 Codelab 2
from tkinter import *
import random
from tkinter import messagebox

tries = 1 #if number of tries goes up, points of the answer will be cut in half
questions_for_quiz = 10 # how many questions will there be for each difficulty

#Function Keys Section
def displayResults():
    holder

def decideOperation():#creates a 50/50 on deciding which operation should be used
    return random.choice(["+", "-"])
    print(decideOperation)#testing purposes on another python file; note to self - delete after finalising

def displayProblem():
    holder

def randomInt(max_num):
    return random.randint(1, max_num)

def back_menu(menu):
    go_back = messagebox.askyesno("Confirm","Do you want to go back to the menu?")
    if go_back:
        menu.destroy()


def destroy():
    answer = messagebox.askyesno("Exit", "Would you like to close the app?")
    if answer:
        root.destroy()

def displayMenu():
    menu=Toplevel(root)
    menu.title("Difficulty")
    menu.geometry("800x500")
    menu.config(bg="#22628e")

    def quizTab(difficulty):
        for w in menu.winfo_children():#code referenced from deepseek
            w.destroy()
        menu.title(f"{difficulty} Quiz")

        Label(menu, text="Question Label", font=("Tahoma", 24, "bold"), bg="#22628e", fg="white").pack(pady=20) #This will display how many questions there are left
        Label(menu, text="Score Label", font=("Tahoma", 16), bg="#22628e", fg="white").pack()# How much score the user gets in total
        Label(menu, text="Problem Label", font=("Tahoma", 16, "bold"), bg="#22628e", fg="white").pack(pady=20)# The problem that the user has to solve
        answer = Entry(menu, font=("Tahoma", 24, "bold"), fg="white").pack(pady=20)# The entry for the user can type their answer
        def returntoMenu():
            for w in menu.winfo_children():#code referenced from deepseek
                w.destroy()
            menu.title("Difficulty")
            Label(menu, text="Choose your difficulty", font=("Tahoma", 24, "bold"), bg="#22628e", fg="white").pack(pady=20)
                
            Button(menu, text="Easy", font=("Tahoma", 20, "bold"), bg="#22628e", width=15, command=lambda: quizTab("Easy")).pack(pady=20)#single digit quiz
            Button(menu, text="Moderate", font=("Tahoma", 20, "bold"), bg="#22628e", width=15, command=lambda: quizTab("Moderate")).pack(pady=20)#2-digit quiz    
            Button(menu, text="Advanced", font=("Tahoma", 20, "bold"), bg="#22628e", width=15, command=lambda: quizTab("Advanced")).pack(pady=20)#4-digit quiz
            
            Button(menu, text="Go Back", font=("Tahoma", 20, "bold"), bg="#22628e", width=5, command=lambda:back_menu(menu)).pack(pady=20)
        
        Button(menu, text="Submit", font=("Tahoma", 20, "bold"), bg="#22628e", width=5).pack(pady=20)#Button to submit your answer
        Button(menu, text="Go Back", font=("Tahoma", 20, "bold"), bg="#22628e", width=5, command=returntoMenu).pack(pady=20)#Goes back to difficulty menu


    Label(menu, text="Choose your difficulty", font=("Tahoma", 24, "bold"), bg="#22628e", fg="white").pack(pady=20)

    Button(menu, text="Easy", font=("Tahoma", 20, "bold"), bg="#22628e", width=15, command=lambda: quizTab("Easy")).pack(pady=20)#single digit quiz
    Button(menu, text="Moderate", font=("Tahoma", 20, "bold"), bg="#22628e", width=15, command=lambda: quizTab("Moderate")).pack(pady=20)#2-digit quiz
    Button(menu, text="Advanced", font=("Tahoma", 20, "bold"), bg="#22628e", width=15, command=lambda: quizTab("Advanced")).pack(pady=20)#4-digit quiz

    Button(menu, text="Go Back", font=("Tahoma", 20, "bold"), bg="#22628e", width=5, command=lambda:back_menu(menu)).pack(pady=20)

        


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


print(randomInt(999))#test the randomizer
root.mainloop()
