import tkinter as tk
from controlFrame import ControlFrame


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Conversor de Temperatura")
        self.geometry("340x150")
        

if __name__ == "__main__":
    app = App()
    ControlFrame(app)
    app.mainloop()