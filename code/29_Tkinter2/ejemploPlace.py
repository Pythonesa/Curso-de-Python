import tkinter as tk

root = tk.Tk()
root.title("Ejemplo con Place")

label1 = tk.Label(root, text="pos absoluta", background="red", foreground="white")
label1.place(x=20, y=10)

label2 = tk.Label(root, text="pos relativa", background="blue", foreground="white")
label2.place(relx=0.8, rely=0.2, anchor=tk.NE)

root.mainloop()