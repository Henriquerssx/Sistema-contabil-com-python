# app/telas/tela_relatorios.py
import tkinter as tk
from app.style import COLORS, FONTS

class TelaRelatorios(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(bg=COLORS["background"])
        
        main_container = tk.Frame(self, bg=COLORS["content_bg"], padx=20, pady=20)
        main_container.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(main_container, text="Relatórios Financeiros", font=FONTS["title"], bg=COLORS["content_bg"], fg=COLORS["text"]).pack(anchor="w")
        tk.Label(main_container, text="Analise a evolução das suas finanças com gráficos detalhados.", font=FONTS["body"], bg=COLORS["content_bg"], fg=COLORS["text"]).pack(anchor="w", pady=(0, 20))

        tk.Label(main_container, text="[Gráficos de pizza, barras e filtros de data virão aqui]", font=FONTS["body"], bg=COLORS["content_bg"], fg="#95a5a6").pack(pady=50)