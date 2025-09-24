from datetime import datetime

class Movimentacao:
    def __init__(self, id, data, descricao, tipo, valor, categoria):
        self.id = id
        self.data = data
        self.descricao = descricao
        self.tipo = tipo
        self.valor = valor
        self.categoria = categoria