# app/telas/tela_sugestoes.py
import tkinter as tk
from app.style import COLORS, FONTS

class TelaSugestoes(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(bg=COLORS["background"])
        
        main_container = tk.Frame(self, bg=COLORS["content_bg"], padx=20, pady=20)
        main_container.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(main_container, text="Sugestões Financeiras", font=FONTS["title"], bg=COLORS["content_bg"], fg=COLORS["text"]).pack(anchor="w")
        tk.Label(main_container, text="Dicas personalizadas para melhorar sua saúde financeira.", font=FONTS["body"], bg=COLORS["content_bg"], fg=COLORS["text"]).pack(anchor="w", pady=(0, 20))

        card = tk.Frame(main_container, bg=COLORS["background"], relief="solid", bd=1, padx=15, pady=15)
        card.pack(fill="x", pady=10)
        tk.Label(card, text="💡 Oportunidade de Economia", font=FONTS["header"], bg=COLORS["background"], fg=COLORS["primary"]).pack(anchor="w")
        tk.Label(card, text="Notamos que seus gastos com 'Lazer' aumentaram 20% este mês. Considere explorar opções de entretenimento gratuitas.", font=FONTS["body"], bg=COLORS["background"], wraplength=800, justify="left").pack(anchor="w", pady=5)