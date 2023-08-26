import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Login con Grid")
root.geometry("400x400")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

lbl_nick = ttk.Label(root, text="Nick:")
lbl_nick.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)

nick = ttk.Entry(root)
nick.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

lbl_pass = ttk.Label(root, text="Password:")
lbl_pass.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

password = ttk.Entry(root, show="*")
password.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

btn_login = ttk.Button(root, text="Login")
btn_login.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)


root.mainloop()