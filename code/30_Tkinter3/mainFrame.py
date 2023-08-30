import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

class MainFrame(ttk.Frame):
    def __init__(self, contenedor, unidad, conversor):
        super().__init__(contenedor)
        self.unidad = unidad
        self.conversor = conversor
        
        opciones = {"padx": 5, "pady": 0}
        
        self.temperatura_label = ttk.Label(self, text=self.unidad)
        self.temperatura_label.grid(row=0, column=0, sticky=tk.W, **opciones)
        
        self.temperatura = tk.StringVar()
        self.temperatura_entry = ttk.Entry(self, textvariable=self.temperatura)
        self.temperatura_entry.grid(row=0, column=1, sticky=tk.W, **opciones)
        self.temperatura_entry.focus()
        
        self.convertir_button = ttk.Button(self, text="Convertir")
        self.convertir_button.grid(row=0, column=2, sticky=tk.W, **opciones)
        self.convertir_button.configure(command=self.convertir)
        
        self.resultado = ttk.Label(self)
        self.resultado.grid(row=1, column=0, columnspan=3, **opciones)
        
        self.grid(column=0, row=0, sticky=tk.NSEW, padx=5, pady=5)
        
    
    def convertir(self, event=None):
        try:
            valor = float(self.temperatura.get())
            resultado = self.conversor(valor)
            self.resultado.configure(text=resultado)
        except ValueError as error:
            showerror("Error", error)
            
    
    def resetear(self):
        self.temperatura_entry.delete(0, tk.END)
        self.resultado.configure(text="")
        self.resultado.text = ""