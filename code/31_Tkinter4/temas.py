import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Temas")
        
        self.estilo = ttk.Style()
        
        self.selected_item = tk.StringVar()
        frame_temas = ttk.LabelFrame(self, text="Temas")
        frame_temas.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        
        for nombre in self.estilo.theme_names():
            rb = ttk.Radiobutton(
                frame_temas,
                text=nombre, 
                value=nombre, 
                variable=self.selected_item, 
                command=self.change_theme)
            rb.pack(expand=True, fill=tk.BOTH)
            
        boton = ttk.Button(self, text="Un botón")
        boton.grid(row=1, column=0, padx=10, pady=10)
        boton2 = ttk.Button(self, text="Otro botón", style="Boton.TButton")
        boton2.grid(row=2, column=0, padx=10, pady=10)
        print(boton.winfo_class())
        
        self.estilo.configure("TButton", foreground="purple", font=("Hack", 16))
        self.estilo.map("TButton",
                        foreground=[
                            ("pressed", "red"),
                            ("active", "green")
                        ])
        self.estilo.configure("Boton.TButton", foreground="blue", font=("Hack", 18))
        
        
        print(self.estilo.layout("TLabel"))
        print(self.estilo.element_options("TLabel.border"))
        print(self.estilo.element_options("TLabel.padding"))
        print(self.estilo.element_options("TLabel.label"))
        print(self.estilo.lookup("TLabel.label", "background"))
            
    def change_theme(self):
        self.estilo.theme_use(self.selected_item.get())
        
if __name__ == "__main__":
    app = App()
    app.mainloop()