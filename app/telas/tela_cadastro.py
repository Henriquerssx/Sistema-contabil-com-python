# app/telas/tela_cadastro.py
import tkinter as tk
from tkinter import messagebox
from app.user_dao import UserDAO
from app.style import COLORS, FONTS

class TelaCadastro(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.user_dao = UserDAO()
        self.configure(bg=COLORS["background"])

        tk.Label(self, text="ZENTRO", font=("Segoe UI", 16, "bold"), fg=COLORS["sidebar_bg"], bg=COLORS["background"]).pack(pady=(50, 0))
        tk.Label(self, text="Crie sua Conta", font=FONTS["large_title"], fg=COLORS["text"], bg=COLORS["background"]).pack(pady=(10, 40))
        
        tk.Label(self, text="Usuário", font=FONTS["body"], bg=COLORS["background"]).pack(pady=(10, 0))
        self.username_entry = tk.Entry(self, font=FONTS["body"], width=35, relief="solid", bd=1)
        self.username_entry.pack(pady=5, ipady=4)

        tk.Label(self, text="Senha", font=FONTS["body"], bg=COLORS["background"]).pack(pady=(10, 0))
        self.password_entry = tk.Entry(self, font=FONTS["body"], width=35, show="*", relief="solid", bd=1)
        self.password_entry.pack(pady=5, ipady=4)

        self.register_button = tk.Button(self, text="CADASTRAR", font=FONTS["body_bold"], bg=COLORS["primary"], fg=COLORS["text_light"], relief="flat", width=30, pady=5, command=self.register_user)
        self.register_button.pack(pady=20)
        self.register_button.bind("<Enter>", lambda e: self.register_button.config(bg=COLORS["primary_dark"]))
        self.register_button.bind("<Leave>", lambda e: self.register_button.config(bg=COLORS["primary"]))

        self.login_button = tk.Button(self, text="Já tem uma conta? Faça o login", font=FONTS["small"], bg=COLORS["background"], fg="blue", bd=0, relief="flat", command=lambda: controller.show_frame("TelaLogin"))
        self.login_button.pack()

    def register_user(self):
        usuario = self.username_entry.get()
        senha = self.password_entry.get()
        if not usuario or not senha:
            return messagebox.showerror("Erro", "Usuário e senha são obrigatórios.")
        if self.user_dao.add_user(usuario, senha):
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            self.controller.show_frame("TelaLogin")
        else:
            messagebox.showerror("Erro", "Este nome de usuário já existe.")