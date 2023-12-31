import random
from tkinter import *

x=Tk()
x.title("Rps")
x.geometry("400x250")
option=["Rock","Paper","Scissor"]
user_s,comp_s,tie_s=0,0,0
def score():
    y=Tk()
    y.title("Score")

    label1=Label(y,text="User ",font=("bold"),fg="red")
    label2=Label(y,text="Computer ",font=("bold"),fg="red")
    label3=Label(y,text="Tie ",font=("bold"),fg="red")

    label1.grid(row=0,column=0)
    label2.grid(row=0,column=2)
    label3.grid(row=0,column=4)

    score_user=Label(y,text=str(user_s),font=("bold"))
    score_computer=Label(y,text=str(comp_s),font=("bold"))
    score_tie=Label(y,text=str(tie_s),font=("bold"))

    score_user.grid(row=2,column=0)
    score_computer.grid(row=2,column=2)
    score_tie.grid(row=2,column=4)
    
    y.mainloop()
def show(choice):
    global user_s
    global comp_s
    global tie_s
    comp_choice=random.choice(option)
    label_user.config(text=choice)
    label_computer.config(text=comp_choice)
    if choice==comp_choice:
        tie_s+=1
        entry.delete(0,"end")
        entry.insert(0,"Tie")
        entry.config(highlightbackground="black",highlightcolor="black")
    else:
        wins=0
        if choice=="Rock" and comp_choice=="Scissor":
            wins=1
        elif choice=="Paper" and comp_choice =="Rock":
            wins=1
        elif choice=="Scissor" and comp_choice=="Paper":
            wins=1

                
        if wins==0:
            comp_s+=1
            entry.delete(0,"end")
            entry.insert(0,"Computer wins")
            entry.config(highlightbackground="red",highlightcolor="red")
        else:
            user_s+=1
            entry.delete(0,"end")
            entry.insert(0,"User wins")
            entry.config(highlightbackground="green",highlightcolor="green")
    
label_user=Label(x,text="User",font=("bold"))
label_vs=Label(x,text="VS",font=("bold"),fg="blue")
label_computer=Label(x,text="Computer",font=("bold"))

label_user.place(x=80,y=40)
label_vs.place(x=175,y=40)
label_computer.place(x=250,y=40)

entry=Entry(x,highlightthickness=2,highlightbackground="black",highlightcolor="black",justify=CENTER)
entry.place(x=130,y=95)
entry.insert(0,"Winner")

label=Label(x,text="Choose your choice : Rock,Paper,Scissor")
label.place(x=90,y=140)

button_rock=Button(x,text="Rock",command=lambda:show("Rock"))
button_paper=Button(x,text="Paper",command=lambda:show("Paper"))
button_scissor=Button(x,text="Scissor",command=lambda:show("Scissor"))
button_score=Button(x,text="Show Score",command=score,bg="#FFD700")

button_rock.place(x=110,y=170)
button_paper.place(x=170,y=170)
button_scissor.place(x=230,y=170)
button_score.place(x=155,y=210)

x.mainloop()
