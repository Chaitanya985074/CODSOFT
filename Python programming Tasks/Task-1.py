# TO-DO LIST APPLICATION

import tkinter as tk

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        listbox_task.delete(0, tk.END)

def update_task():
    selected_task = listbox_tasks.curselection()
    if selected_task:
        task = entry_task.get()
        listbox_task.delete(selected_task)
        listbox_task.insert(selected_task, task)
        entry_task.delete(0, tk.END)

root=tk.Tk()
root.title("TO-DO LIST APPLICATION")

entry_task = tk.Entry(root, width=50)
entry_task.pack()

listbox_tasks = tk.Listbox(root, height=10, width=50)
listbox_tasks.pack()

button_add = tk.Button(root, text="Add Task", width=50, command=add_task)
button_add.pack()

button_update = tk.Button(root, text="Update Task", width=50, command=update_task)
button_update.pack()

root.mainloop()
