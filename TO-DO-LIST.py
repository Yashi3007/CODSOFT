import tkinter as tk
from tkinter import simpledialog, messagebox
tasks = []

def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        update_task_display()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    task_to_delete = simpledialog.askstring("Delete Task", "Enter the task which you want to delete:")
    if task_to_delete in tasks:
        tasks.remove(task_to_delete)
        update_task_display()
    else:      
        messagebox.showwarning("Warning", "Task not found!!! Please enter a correct task")

def update_task_display():
    task_text = "\n".join(f"- {task}" for task in tasks)
    label_tasks.config(text=task_text)

window = tk.Tk()
window.title("To-Do List")
window.config(bg="beige")
window.resizable(0,0)

frame_input = tk.Frame(window)
frame_input.pack(padx=100,pady=10)
frame_header = tk.Frame(window, bg="beige", pady=10, relief="flat")
frame_header.pack(fill=tk.X)
header = tk.Label(frame_header, text="To-Do List", font=("Lucida Calligraphy", 30, "underline"), bg="beige", fg="red")
header.pack()
frame_input = tk.Frame(window, bg="beige", padx=15, pady=15, borderwidth=10, relief="flat")
frame_input.pack(padx=10,pady=10, fill=tk.X)


tk.Label(frame_input, text="Task:",font=("Times New Roman",20,"bold"),fg="black",bg="white",relief="flat").pack(side=tk.LEFT, padx=10)
entry_task = tk.Entry(frame_input, width=40)
entry_task.pack(side=tk.LEFT)

button_add_task = tk.Button(frame_input, text="Add Task", font=("Times New Roman",18,"bold"),fg="yellow",bg="green",relief="flat",command=add_task)
button_add_task.pack(side=tk.LEFT)

button_delete_task = tk.Button(frame_input, text="Delete Task", font=("Times New Roman",18,"bold"),fg="yellow",bg="red",relief="flat", command=delete_task)
button_delete_task.pack(side=tk.LEFT, padx=10,pady=10)

label_tasks = tk.Label(window, text="", justify=tk.LEFT, font=("Times New Roman",18,"bold"),fg="black",bg="beige", relief="flat",padx=250, pady=100)
label_tasks.pack()
window.mainloop()
