from tkinter import *
from tkinter import ttk
from tkinter import messagebox
sno=0

x=Tk()
x.title("To Do List")
x.geometry("700x350")
def select_rec(m):
    clear()
    t_s_1=tree.selection()
    t_f_1=tree.focus()
    t_i_1=tree.item(t_f_1,"values")
    if len(t_i_1)==0:
        pass
    else:
        task_box.insert("0.0",t_i_1[1])
def create():
    global sno
    if len(task_box.get("1.0",END))==1:
        messagebox.showinfo("","Error : No Task Entered")
    else:
        sno+=1
        tree.insert('', 'end', values=(sno,task_box.get("1.0",END),"Incomplete"))
        clear()
def update():
    clear()
    s=tree.focus()
    v=tree.item(s,"values")
    if len(v)!=0:
        tree.item(s,values=(v[0],v[1],"Completed"))
def modify():
    s=tree.focus()
    v=tree.item(s,"values")
    if len(v)!=0:
        yn=messagebox.askyesno("","Do you want to modify the task")
        if yn==True:
            tree.item(s,values=(v[0],task_box.get("1.0",END),v[2]))
            clear()
def clear():
    task_box.delete("1.0",END)
    
st=ttk.Style()
st.theme_use("default")
st.configure("treeview",background="#D3D3D3",foreground="black",rowheight=25,fieldbackground="#D3D3D3")
st.map("treeview",background=[("selected","#347083")])
t_f=Frame()
t_f.pack(pady=10)
t_s=Scrollbar(t_f)
t_s.pack(side="right",fill="y")

tree=ttk.Treeview(t_f,yscrollcommand=t_s.set,selectmode="extended")
tree.pack()
t_s.config(command=tree.yview)
tree["columns"]=("Sno","Task","Status")
tree.column("#0",width=0,stretch="no")
tree.column("Sno",anchor="w",width=130)
tree.column("Task",anchor="w",width=400)
tree.column("Status",anchor="center",width=140)

tree.heading("#0",text="",anchor="w")
tree.heading("Sno",text="Sno",anchor="w")
tree.heading("Task",text="Task",anchor="center")
tree.heading("Status",text="Status",anchor="w")

label_task=Label(x,text="Task : ")
label_task.place(x=10,y=280)

task_box=Text(x,width=30,height=5,highlightthickness=1,highlightbackground = "black", highlightcolor= "black")
task_box.place(x=50,y=250)

button_create=Button(x,text="Create Task",command=create,fg="blue")
button_update=Button(x,text="Mark Complete",command=update,fg="blue")
button_modify=Button(x,text="Modify Task",command=modify,fg="blue")

button_create.place(x=350,y=275)
button_update.place(x=440,y=275)
button_modify.place(x=550,y=275)


tree.bind("<ButtonRelease-1>",select_rec)

x.mainloop()
