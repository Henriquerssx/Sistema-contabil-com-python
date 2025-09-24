# app/telas/tela_metas.py
import tkinter as tk
from tkinter import ttk
from app.style import COLORS, FONTS

class TelaMetas(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(bg=COLORS["background"])
        
        main_container = tk.Frame(self, bg=COLORS["content_bg"], padx=20, pady=20)
        main_container.pack(fill="both", expand=True, padx=20, pady=20)

        header_frame = tk.Frame(main_container, bg=COLORS["content_bg"])
        header_frame.pack(fill="x", pady=(0, 20))

        tk.Label(header_frame, text="Metas Financeiras", font=FONTS["title"], bg=COLORS["content_bg"], fg=COLORS["text"]).pack(side="left")
        
        add_button = tk.Button(header_frame, text="+ Nova Meta", font=FONTS["body_bold"], bg=COLORS["primary"], fg=COLORS["text_light"], relief="flat")
        add_button.pack(side="right")
        add_button.bind("<Enter>", lambda e: add_button.config(bg=COLORS["primary_dark"]))
        add_button.bind("<Leave>", lambda e: add_button.config(bg=COLORS["primary"]))

        meta_frame = tk.Frame(main_container, bg=COLORS["background"], bd=1, relief="solid")
        meta_frame.pack(fill="x", pady=10)
        
        tk.Label(meta_frame, text="Viagem para a Praia", font=FONTS["header"], bg=COLORS["background"]).pack(anchor="w", padx=15, pady=(10, 0))
        
        progress_label = tk.Label(meta_frame, text="R$ 1.500,00 / R$ 4.000,00", font=FONTS["body"], bg=COLORS["background"])
        progress_label.pack(anchor="w", padx=15)

        progress_bar = ttk.Progressbar(meta_frame, orient="horizontal", length=300, mode="determinate", value=37.5)
        progress_bar.pack(fill="x", padx=15, pady=(5, 15))