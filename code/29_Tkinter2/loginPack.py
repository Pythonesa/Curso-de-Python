import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Login con Pack")
root.geometry("400x400")

fields = {}

fields["nick_label"] = ttk.Label(root, text="Nick:")
fields["nick_entry"] = ttk.Entry(root)

fields["password_label"] = ttk.Label(root, text="Password:")
fields["password_entry"] = ttk.Entry(root, show="*")

for field in fields.values():
    field.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)
    
ttk.Button(root, text="Login").pack(anchor=tk.W, padx=10, pady=5)

root.mainloop()