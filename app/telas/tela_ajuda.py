# app/telas/tela_ajuda.py
import tkinter as tk
from app.style import COLORS, FONTS

class TelaAjuda(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(bg=COLORS["background"])
        
        main_container = tk.Frame(self, bg=COLORS["content_bg"], padx=20, pady=20)
        main_container.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(main_container, text="Central de Ajuda", font=FONTS["title"], bg=COLORS["content_bg"], fg=COLORS["text"]).pack(anchor="w")
        tk.Label(main_container, text="Encontre respostas para as suas dúvidas mais frequentes.", font=FONTS["body"], bg=COLORS["content_bg"], fg=COLORS["text"]).pack(anchor="w", pady=(0, 30))

        tk.Label(main_container, text="Como cadastrar uma nova despesa?", font=FONTS["header"], bg=COLORS["content_bg"]).pack(anchor="w", pady=(10, 5))
        tk.Label(main_container, text="1. Navegue até a tela de 'Saídas' no menu lateral.\n2. Clique no botão '+ Nova Saída'.\n3. Preencha os detalhes da despesa e clique em 'Salvar'.", font=FONTS["body"], bg=COLORS["content_bg"], justify="left").pack(anchor="w")