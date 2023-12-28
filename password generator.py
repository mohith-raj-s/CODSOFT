from tkinter import *
import random

x=Tk()
x.geometry("500x200")
x.title("password generator")
def generate():
    passwd=""
    for i in range(int(entry.get())):
        passwd+=chr(random.randint(33,126))
                 
    label1.config(text="The Password is ",fg="red")
    label_passwd.config(text=passwd,bg="black",font=("bold"))
        
label=Label(x,text="Enter length of the password :")
label.place(x=170,y=40)

entry=Entry(x)
entry.place(x=190,y=70)

button=Button(x,text="Generate",command=generate)
button.place(x=360,y=65)

label1=Label(x,text="")
label1.place(x=10,y=120)
 
label_passwd=Label(x,text="",fg="white")
label_passwd.place(x=100,y=120)

x.mainloop()
