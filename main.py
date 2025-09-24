# main.py

# --- INÍCIO DA CORREÇÃO ---
import sys
import os

# Adiciona a pasta raiz do projeto (Sistema contabil com python) ao sys.path
# Isso garante que o Python encontre a pasta 'app'
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(PROJECT_ROOT)
# --- FIM DA CORREÇÃO ---

import tkinter as tk
from app.telas.tela_login import TelaLogin
from app.telas.tela_cadastro import TelaCadastro
from app.telas.tela_dashboard import TelaDashboard

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ZENTRO FINops")
        self.geometry("1200x800")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (TelaLogin, TelaCadastro, TelaDashboard):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("TelaLogin")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()