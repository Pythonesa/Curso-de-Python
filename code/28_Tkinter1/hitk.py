import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Hola Mundo")
root.geometry("600x400+50+50")
root.resizable(False, False)

icono = ImageTk.PhotoImage(Image.open("hi.png"))
root.wm_iconphoto(True, icono)

lblMessage = ttk.Label(root, text="¡Hola Mundo!")
lblMessage.pack()


def btn_chau_clicked(event):
    lblMessage["text"] = "¡Chau mundo!"
    
def log_chau(event):
    print("Chau mundo!")

#btnChau = ttk.Button(root, text="Chau", command=btn_chau_clicked).pack()
btnChau = ttk.Button(root, text="Chau")
btnChau.bind("<ButtonPress>", btn_chau_clicked)
btnChau.bind("<ButtonRelease>", log_chau, add="+")
btnChau.pack()


root.mainloop()