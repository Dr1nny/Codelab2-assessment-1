# Exercise 1 Codelab 2
from tkinter import *
import random
from tkinter import messagebox

questions_for_quiz = 10 # how many questions will there be for each difficulty

#Function Keys Section
def displayResults():
    holder

def decideOperation():#creates a 50/50 on deciding which operation should be used
    return random.choice(["+", "-"])

def displayProblem(difficulty, menu):
    if difficulty == "Easy":
        max_num = 9 #When selecting easy, the maximum number that the random can go to is 9.
    elif difficulty == "Moderate":
        max_num = 99 #Does the same thing for easy but allows 2-digits instead on single digits
    else:
        max_num = 9999 #Allows 4-digits for advanced button.
    
    a = randomInt(max_num)#Holds a random number in this variable
    b = randomInt(max_num)#Holds another random number for this variable
    op = decideOperation()#Decides whether if the symbol is "+" or "-", a coin-flip
    correct = a + b if op == '+' else a - b#Computes the answer based on the stored operation

    Label(menu, text=f"{a} {op} {b} = ?", font=("Tahoma", 16, "bold"),bg="#22628e", fg="white").pack(pady=20)
    answer = Entry(menu, font=("Tahoma", 24, "bold"), fg="white")# The entry for the user can type their answer
    answer.pack(pady=20)

    return answer, correct

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
        tries = 1 #if number of tries goes up, points of the answer will be cut in half
        for w in menu.winfo_children():#code referenced from deepseek
            w.destroy()
        menu.title(f"{difficulty} Quiz")

        Label(menu, text=f"Question 1 out of {questions_for_quiz}", font=("Tahoma", 24, "bold"), bg="#22628e", fg="white").pack(pady=20) #This will display how many questions there are left
        Label(menu, text="Score: 0", font=("Tahoma", 16), bg="#22628e", fg="white").pack()# How much score the user gets in total

        answer_entry, correct_answer = displayProblem(difficulty, menu)

        def submit():#Creates a function for submit button to work
            nonlocal tries#binds to quizTab function's tries.

            try:
                user_val = int(answer_entry.get())
            except ValueError:
                messagebox.showwarning("Invalid", "Please enter a number.")
                return
            if user_val == correct_answer:
                messagebox.showinfo("Correct!", "Nice work!")
                
            else:
                tries += 1
                if tries <= 2:
                    messagebox.showwarning("Try again", "One more try.")
                    answer_entry.delete(0, END)
                    answer_entry.focus_set()
                else:
                    messagebox.showerror("Wrong", f"The answer was {correct_answer}.")
        
        def returntoMenu():
            for w in menu.winfo_children():#code referenced from deepseek
                w.destroy()
            menu.title("Difficulty")
            Label(menu, text="Choose your difficulty", font=("Tahoma", 24, "bold"), bg="#22628e", fg="white").pack(pady=20)
                
            Button(menu, text="Easy", font=("Tahoma", 20, "bold"), fg="#2d8e22", width=15, command=lambda: quizTab("Easy")).pack(pady=20)#single digit quiz
            Button(menu, text="Moderate", font=("Tahoma", 20, "bold"), fg="#dee10e", width=15, command=lambda: quizTab("Moderate")).pack(pady=20)#2-digit quiz    
            Button(menu, text="Advanced", font=("Tahoma", 20, "bold"), fg="#8e2222", width=15, command=lambda: quizTab("Advanced")).pack(pady=20)#4-digit quiz
            
            Button(menu, text="Go Back", font=("Tahoma", 20, "bold"), bg="#22628e", width=5, command=lambda:back_menu(menu)).pack(pady=20)
        
        Button(menu, text="Submit", font=("Tahoma", 20, "bold"), bg="#22628e", width=5, command=submit).pack(pady=20)#Button to submit your answer
        Button(menu, text="Go Back", font=("Tahoma", 20, "bold"), bg="#22628e", width=5, command=returntoMenu).pack(pady=20)#Goes back to difficulty menu


    Label(menu, text="Choose your difficulty", font=("Tahoma", 24, "bold"), bg="#22628e", fg="white").pack(pady=20)

    Button(menu, text="Easy", font=("Tahoma", 20, "bold"), fg="#2d8e22", width=15, command=lambda: quizTab("Easy")).pack(pady=20)#single digit quiz
    Button(menu, text="Moderate", font=("Tahoma", 20, "bold"), fg="#dee10e", width=15, command=lambda: quizTab("Moderate")).pack(pady=20)#2-digit quiz
    Button(menu, text="Advanced", font=("Tahoma", 20, "bold"), fg="#8e2222", width=15, command=lambda: quizTab("Advanced")).pack(pady=20)#4-digit quiz

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
