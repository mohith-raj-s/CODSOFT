from tkinter import *
from tkinter import messagebox

x=Tk()
x.title("calc")

operator=0

def show(char):
    global operator
    curr=entry.get()
    entry.delete(0,'end')
    entry.insert(0,str(curr)+str(char))
    if char in ["+","-","*","/","%"]:
        operator=len(entry.get())-1
def clear():
    entry.delete(0,'end')
def compute():
    m=entry.get()
    if len(m)!=0:
        if m[operator] not in ["+","-","*","/","%"]:
            messagebox.showinfo("","Error : No operator specified")
        elif operator==0 or operator==len(m)-1:
            messagebox.showinfo("","Error : Invalid format")
        else:
            num1=int(m[0:operator])
            num2=int(m[operator+1:])
            result=0
            if m[operator]=="+":
                result=num1+num2
            elif m[operator]=="-":
                result=num1-num2
            elif m[operator]=="*":
                result=num1*num2
            elif m[operator]=="/":
                result=num1/num2
            else:
                result=num1%num2
            clear()
            entry.insert(0,result)
    else:
        messagebox.showinfo("","Error : No value provided")

entry=Entry(x,width=40)
entry.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

button_mod=Button(x,text="%",padx=10,pady=10,width=5,bg="grey",command=lambda:show("%"))
button_div=Button(x,text="/",padx=10,pady=10,width=5,bg="grey",command=lambda:show("/"))
button_prod=Button(x,text="*",padx=10,pady=10,width=5,bg="grey",command=lambda:show("*"))
button_sub=Button(x,text="-",padx=10,pady=10,width=5,bg="grey",command=lambda:show("-"))
button_1=Button(x,text="1",padx=10,pady=10,width=5,command=lambda:show(1))
button_2=Button(x,text="2",padx=10,pady=10,width=5,command=lambda:show(2))
button_3=Button(x,text="3",padx=10,pady=10,width=5,command=lambda:show(3))
button_4=Button(x,text="4",padx=10,pady=10,width=5,command=lambda:show(4))
button_5=Button(x,text="5",padx=10,pady=10,width=5,command=lambda:show(5))
button_6=Button(x,text="6",padx=10,pady=10,width=5,command=lambda:show(6))
button_7=Button(x,text="7",padx=10,pady=10,width=5,command=lambda:show(7))
button_8=Button(x,text="8",padx=10,pady=10,width=5,command=lambda:show(8))
button_9=Button(x,text="9",padx=10,pady=10,width=5,command=lambda:show(9))
button_0=Button(x,text="0",padx=20,pady=10,width=12,command=lambda:show(0))
button_clear=Button(x,text="C",padx=10,pady=10,width=5,fg="red",command=clear)
button_add=Button(x,text="+",padx=10,pady=22,width=5,height=2,bg="grey",command=lambda:show("+"))
button_eq=Button(x,text="=",padx=10,pady=24,width=5,height=2,bg="grey",command=compute)

button_mod.grid(row=1,column=0)
button_div.grid(row=1,column=1)
button_prod.grid(row=1,column=2)
button_sub.grid(row=1,column=3)
button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_0.grid(row=5,column=0,columnspan=2)
button_clear.grid(row=5,column=2)
button_add.grid(row=2,column=3,rowspan=2)
button_eq.grid(row=4,column=3,rowspan=2)

x.mainloop()
