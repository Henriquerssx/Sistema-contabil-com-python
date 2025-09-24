# app/telas/tela_dashboard.py
import tkinter as tk
from app.style import COLORS, FONTS
from app.telas.tela_visao_geral import TelaVisaoGeral
from app.telas.tela_entradas import TelaEntradas
from app.telas.tela_saidas import TelaSaidas
from app.telas.tela_metas import TelaMetas
from app.telas.tela_categorias import TelaCategorias
from app.telas.tela_relatorios import TelaRelatorios
from app.telas.tela_sugestoes import TelaSugestoes
from app.telas.tela_configuracoes import TelaConfiguracoes
from app.telas.tela_ajuda import TelaAjuda

class TelaDashboard(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # --- Menu Lateral ---
        menu_lateral = tk.Frame(self, width=250, bg=COLORS["sidebar_bg"])
        menu_lateral.pack(side="left", fill="y")
        
        tk.Label(menu_lateral, text="ZENTRO", font=FONTS["title"], bg=COLORS["sidebar_bg"], fg=COLORS["text_light"]).pack(pady=30, padx=20)
        
        botoes_menu = {
            "Visão Geral": "TelaVisaoGeral",
            "Entradas": "TelaEntradas",
            "Saídas": "TelaSaidas",
            "Relatórios": "TelaRelatorios",
            "Metas": "TelaMetas",
            "Sugestões": "TelaSugestoes",
            "Categorias": "TelaCategorias",
            "Configurações": "TelaConfiguracoes",
            "Ajuda": "TelaAjuda",
        }
        
        for texto, tela in botoes_menu.items():
            btn = tk.Button(menu_lateral, text=texto, font=FONTS["body_bold"], bg=COLORS["sidebar_bg"], fg=COLORS["text_light"], bd=0, relief="flat", anchor="w",
                             command=lambda t=tela: self.show_content(t))
            btn.pack(fill="x", pady=5, padx=20)
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=COLORS["primary"]))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=COLORS["sidebar_bg"]))

        logout_button = tk.Button(menu_lateral, text="Logout", font=FONTS["body_bold"], bg=COLORS["danger"], fg=COLORS["text_light"], bd=0, relief="flat",
                                  command=lambda: controller.show_frame("TelaLogin"))
        logout_button.pack(side="bottom", fill="x", pady=20, ipady=5)
        logout_button.bind("<Enter>", lambda e: logout_button.config(bg=COLORS["danger_dark"]))
        logout_button.bind("<Leave>", lambda e: logout_button.config(bg=COLORS["danger"]))

        # --- Área de Conteúdo ---
        self.area_conteudo = tk.Frame(self, bg=COLORS["background"])
        self.area_conteudo.pack(side="right", fill="both", expand=True)
        self.area_conteudo.grid_rowconfigure(0, weight=1)
        self.area_conteudo.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        telas = (TelaVisaoGeral, TelaEntradas, TelaSaidas, TelaRelatorios, TelaMetas, TelaSugestoes, TelaCategorias, TelaConfiguracoes, TelaAjuda)
        
        for F in telas:
            page_name = F.__name__
            frame = F(self.area_conteudo, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_content("TelaVisaoGeral")

    def show_content(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()