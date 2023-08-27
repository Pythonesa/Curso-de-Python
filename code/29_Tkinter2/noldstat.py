import tkinter as tk
from tkinter import ttk

def mover(event):
    x, y = noldstat.winfo_x(), noldstat.winfo_y()
    if event.keysym == "Up":
        y -= 10
    elif event.keysym == "Down":
        y += 10
    elif event.keysym == "Left":
        x -= 10
    elif event.keysym == "Right":
        x += 10

    noldstat.place(x=x, y=y)


root = tk.Tk()
root.title("Noldstat se mueve")
root.geometry("600x400")

noldstat = ttk.Label(root, text="Noldstat", background="green", foreground="white")
noldstat.place(x=50, y=50)

root.bind("<Key>", mover)

root.mainloop()