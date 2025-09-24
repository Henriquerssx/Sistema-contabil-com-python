# app/telas/tela_configuracoes.py
import tkinter as tk
from app.style import COLORS, FONTS

class TelaConfiguracoes(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(bg=COLORS["background"])
        
        main_container = tk.Frame(self, bg=COLORS["content_bg"], padx=20, pady=20)
        main_container.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(main_container, text="Configurações", font=FONTS["title"], bg=COLORS["content_bg"], fg=COLORS["text"]).pack(anchor="w")
        tk.Label(main_container, text="Ajuste as preferências da sua conta e da aplicação.", font=FONTS["body"], bg=COLORS["content_bg"], fg=COLORS["text"]).pack(anchor="w", pady=(0, 30))

        tk.Label(main_container, text="Alterar Senha", font=FONTS["header"], bg=COLORS["content_bg"]).pack(anchor="w", pady=(10, 5))
        tk.Entry(main_container, font=FONTS["body"], width=35, show="*", relief="solid", bd=1).pack(anchor="w", pady=5, ipady=4)
        
        save_button = tk.Button(main_container, text="Salvar Alterações", font=FONTS["body_bold"], bg=COLORS["primary"], fg=COLORS["text_light"], relief="flat", width=20, pady=5)
        save_button.pack(anchor="w", pady=20)
        save_button.bind("<Enter>", lambda e: save_button.config(bg=COLORS["primary_dark"]))
        save_button.bind("<Leave>", lambda e: save_button.config(bg=COLORS["primary"]))