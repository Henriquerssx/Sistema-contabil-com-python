# app/telas/tela_visao_geral.py
import tkinter as tk
from app.style import COLORS, FONTS

class TelaVisaoGeral(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(bg=COLORS["background"])
        
        main_container = tk.Frame(self, bg=COLORS["content_bg"], padx=20, pady=20)
        main_container.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(main_container, text="Visão Geral do Mês", font=FONTS["title"], bg=COLORS["content_bg"], fg=COLORS["text"]).pack(anchor="w")
        tk.Label(main_container, text="Um resumo de suas atividades financeiras no mês atual.", font=FONTS["body"], bg=COLORS["content_bg"], fg=COLORS["text"]).pack(anchor="w", pady=(0, 20))

        summary_frame = tk.Frame(main_container, bg=COLORS["content_bg"])
        summary_frame.pack(fill="x", pady=20)

        card1 = tk.Frame(summary_frame, bg=COLORS["background"], relief="solid", bd=1, padx=15, pady=15)
        card1.pack(side="left", fill="x", expand=True, padx=(0, 10))
        tk.Label(card1, text="Receita Mensal", font=FONTS["header"], bg=COLORS["background"]).pack(anchor="w")
        tk.Label(card1, text="R$ 5.200,00", font=FONTS["title"], fg="#27ae60", bg=COLORS["background"]).pack(anchor="w")

        card2 = tk.Frame(summary_frame, bg=COLORS["background"], relief="solid", bd=1, padx=15, pady=15)
        card2.pack(side="left", fill="x", expand=True, padx=(10, 0))
        tk.Label(card2, text="Despesa Mensal", font=FONTS["header"], bg=COLORS["background"]).pack(anchor="w")
        tk.Label(card2, text="R$ 3.150,00", font=FONTS["title"], fg=COLORS["danger"], bg=COLORS["background"]).pack(anchor="w")
        
        tk.Label(main_container, text="[Gráfico de despesas por categoria virá aqui]", font=FONTS["body"], bg=COLORS["content_bg"], fg="#95a5a6").pack(pady=50)