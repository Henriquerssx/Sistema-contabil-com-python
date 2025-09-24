# app/telas/tela_saidas.py
import tkinter as tk
from app.style import COLORS, FONTS

class TelaSaidas(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(bg=COLORS["background"])
        
        main_container = tk.Frame(self, bg=COLORS["content_bg"], padx=20, pady=20)
        main_container.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(main_container, text="Registro de Saídas", font=FONTS["title"], bg=COLORS["content_bg"], fg=COLORS["text"]).pack(anchor="w")
        tk.Label(main_container, text="Adicione e gerencie suas despesas.", font=FONTS["body"], bg=COLORS["content_bg"], fg=COLORS["text"]).pack(anchor="w", pady=(0, 20))

        tk.Label(main_container, text="[A tabela de saídas e os botões de ação virão aqui]", font=FONTS["body"], bg=COLORS["content_bg"], fg="#95a5a6").pack(pady=50)