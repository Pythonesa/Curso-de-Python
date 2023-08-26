import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Pack")
root.geometry("400x400")

lbl1 = ttk.Label(root, text="Label 1", background="red", foreground="white")
lbl1.configure(anchor=tk.CENTER)
lbl1.pack(ipadx=20, ipady=20, expand=True, side=tk.RIGHT, fill=tk.BOTH)

lbl2 = ttk.Label(root, text="Label 2", background="blue", foreground="white")
lbl2.configure(anchor=tk.CENTER)
lbl2.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)


root.mainloop()