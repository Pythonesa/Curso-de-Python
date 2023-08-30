import tkinter as tk
from tkinter import ttk
from mainFrame import MainFrame
from conversores import ConvertirTemperatura

class ControlFrame(ttk.LabelFrame):
    def __init__(self, contenedor):
        super().__init__(contenedor)
        self["text"] = "Opciones"
        
        self.selected_value = tk.IntVar()
        
        ttk.Radiobutton(self, text="F a C", variable=self.selected_value, value=0, command=self.cambiar_frame).grid(row=0, column=0, padx=5, pady=5)
        ttk.Radiobutton(self, text="C a F", variable=self.selected_value, value=1, command=self.cambiar_frame).grid(row=0, column=1, padx=5, pady=5)
        
        self.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)
        
        self.frames = {}
        self.frames[0] = MainFrame(contenedor, "Fahrenheit", ConvertirTemperatura.fahrenheit_a_celsius)
        self.frames[1] = MainFrame(contenedor, "Celsius", ConvertirTemperatura.celsius_a_fahrenheit)
        self.cambiar_frame()
        
    
    def cambiar_frame(self):
        frame = self.frames[self.selected_value.get()]
        frame.resetear()
        frame.tkraise()