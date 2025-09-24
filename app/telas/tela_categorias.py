# app/telas/tela_categorias.py
import tkinter as tk
from app.style import COLORS, FONTS

class TelaCategorias(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(bg=COLORS["background"])
        
        main_container = tk.Frame(self, bg=COLORS["content_bg"], padx=20, pady=20)
        main_container.pack(fill="both", expand=True, padx=20, pady=20)

        header_frame = tk.Frame(main_container, bg=COLORS["content_bg"])
        header_frame.pack(fill="x", pady=(0, 20))

        tk.Label(header_frame, text="Gerenciar Categorias", font=FONTS["title"], bg=COLORS["content_bg"], fg=COLORS["text"]).pack(side="left")

        add_button = tk.Button(header_frame, text="+ Nova Categoria", font=FONTS["body_bold"], bg=COLORS["primary"], fg=COLORS["text_light"], relief="flat")
        add_button.pack(side="right")
        add_button.bind("<Enter>", lambda e: add_button.config(bg=COLORS["primary_dark"]))
        add_button.bind("<Leave>", lambda e: add_button.config(bg=COLORS["primary"]))

        categorias_frame = tk.Frame(main_container, bg=COLORS["content_bg"])
        categorias_frame.pack(fill="both", expand=True)

        categorias = ["Moradia", "Alimentação", "Transporte", "Lazer", "Salário", "Investimentos"]
        for cat in categorias:
            cat_frame = tk.Frame(categorias_frame, bg=COLORS["background"], height=50, bd=1, relief="solid")
            cat_frame.pack(fill="x", pady=5)
            tk.Label(cat_frame, text=cat, font=FONTS["body"], bg=COLORS["background"]).pack(side="left", padx=15)
            tk.Button(cat_frame, text="Excluir", font=FONTS["small"], fg=COLORS["danger"], relief="flat", bg=COLORS["background"]).pack(side="right", padx=15)
            tk.Button(cat_frame, text="Editar", font=FONTS["small"], relief="flat", bg=COLORS["background"]).pack(side="right")