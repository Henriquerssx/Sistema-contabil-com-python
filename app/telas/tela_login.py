# app/telas/tela_login.py
import tkinter as tk
from tkinter import messagebox
from app.user_dao import UserDAO
from app.criptografia_util import hash_password
from app.style import COLORS, FONTS

class TelaLogin(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.user_dao = UserDAO()

        self.configure(bg=COLORS["background"])

        tk.Label(self, text="ZENTRO", font=("Segoe UI", 16, "bold"), fg=COLORS["sidebar_bg"], bg=COLORS["background"]).pack(pady=(50, 0))
        tk.Label(self, text="Acesse sua conta", font=FONTS["large_title"], fg=COLORS["text"], bg=COLORS["background"]).pack(pady=(10, 40))
        
        tk.Label(self, text="Usuário", font=FONTS["body"], bg=COLORS["background"]).pack(pady=(10, 0))
        self.username_entry = tk.Entry(self, font=FONTS["body"], width=35, relief="solid", bd=1)
        self.username_entry.pack(pady=5, ipady=4)

        tk.Label(self, text="Senha", font=FONTS["body"], bg=COLORS["background"]).pack(pady=(10, 0))
        self.password_entry = tk.Entry(self, font=FONTS["body"], width=35, show="*", relief="solid", bd=1)
        self.password_entry.pack(pady=5, ipady=4)
        
        self.login_button = tk.Button(self, text="ENTRAR", font=FONTS["body_bold"], bg=COLORS["primary"], fg=COLORS["text_light"], relief="flat", width=30, pady=5, command=self.authenticate)
        self.login_button.pack(pady=20)
        self.login_button.bind("<Enter>", lambda e: self.login_button.config(bg=COLORS["primary_dark"]))
        self.login_button.bind("<Leave>", lambda e: self.login_button.config(bg=COLORS["primary"]))

        self.register_button = tk.Button(self, text="Não tem uma conta? Cadastre-se", font=FONTS["small"], bg=COLORS["background"], fg="blue", bd=0, relief="flat", command=lambda: controller.show_frame("TelaCadastro"))
        self.register_button.pack()

    def authenticate(self):
        usuario = self.username_entry.get()
        senha = self.password_entry.get()
        user = self.user_dao.get_user(usuario)
        if user and user['senha_hash'] == hash_password(senha):
            self.controller.show_frame("TelaDashboard")
        else:
            messagebox.showerror("Erro de Login", "Usuário ou senha inválidos.")