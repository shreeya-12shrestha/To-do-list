from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("To-Do-List")
root.geometry("400x600")

a= "#ffb6d6"
b="#ffb6d6"
c ="#ffcce5"
d="#ffa0c8"
e="#ffdceb"
f="#f8aad2"

root.configure(bg=e)

label = Label(root, text="My To-do list", bg=d, fg="white", font=("Arial", 12, "bold"))
label.pack(pady=10)

task = Entry(root, width=30)
task.pack(pady=10)

task_list = Listbox(root, width=40, height=20)
task_list.pack(pady=10)

def add_task():
    task_text = task.get().strip()   
    if task_text != "":
        task_list.insert(END, task_text)
        task.delete(0, END)
        task.focus()

botn = Button(root, text="Add Task", bg=d, fg="white", font=("Arial", 10, "bold"), command=add_task)
botn.pack(pady=5)
def clearr():
    if task_list.size() == 0:
        messagebox.showinfo("Empty", "No tasks to clear")
    else:
        task_list.delete(0, END)

clr_btn = Button(root, text="Clear all", bg=d, fg="white", font=("Arial", 10, "bold"), command=clearr)
clr_btn.pack(pady=5)
def save():
    task = task_list.get(0,END)
    if len(task)==0:
        messagebox.showinfo("No tasks to save")

    with open("task.txt","w", encoding ="utf-8") as f:
        for t in task:
            f.write(t+ "\n")
    messagebox.showinfo("Tasks Saved")
savee = Button(root, text="Save",  bg=d, fg="white", font=("Arial", 10, "bold"),command= save)
savee.pack(pady=5)
root.mainloop()
