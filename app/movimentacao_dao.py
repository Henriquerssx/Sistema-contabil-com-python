# app/movimentacao_dao.py
import sqlite3
import uuid
from datetime import datetime
from app.movimentacao import Movimentacao
from app.database import get_db_connection

class MovimentacaoDAO:
    def get_all(self):
        """Busca todas as movimentações do banco de dados, ordenadas por data."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM movimentacoes ORDER BY data DESC")
        rows = cursor.fetchall()
        conn.close()

        movimentacoes = []
        for row in rows:
            # O formato no banco de dados é 'YYYY-MM-DD HH:MM:SS.ffffff'
            # Removemos os milissegundos para o parse
            data_str = row["data"].split(".")[0]
            movimentacoes.append(
                Movimentacao(
                    id=row["id"],
                    data=datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S"),
                    descricao=row["descricao"],
                    tipo=row["tipo"],
                    valor=row["valor"],
                    categoria=row["categoria"],
                )
            )
        return movimentacoes

    def add(self, movimentacao):
        """Adiciona uma nova movimentação ao banco de dados."""
        movimentacao.id = str(uuid.uuid4())
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO movimentacoes (id, data, descricao, tipo, valor, categoria) VALUES (?, ?, ?, ?, ?, ?)",
            (
                movimentacao.id,
                movimentacao.data,
                movimentacao.descricao,
                movimentacao.tipo,
                movimentacao.valor,
                movimentacao.categoria,
            ),
        )
        conn.commit()
        conn.close()

    def update(self, movimentacao):
        """Atualiza uma movimentação existente no banco de dados."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE movimentacoes SET descricao = ?, tipo = ?, valor = ?, categoria = ? WHERE id = ?",
            (
                movimentacao.descricao,
                movimentacao.tipo,
                movimentacao.valor,
                movimentacao.categoria,
                movimentacao.id,
            ),
        )
        conn.commit()
        conn.close()

    def delete(self, movimentacao_id):
        """Exclui uma movimentação do banco de dados pelo seu ID."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM movimentacoes WHERE id = ?", (movimentacao_id,))
        conn.commit()
        conn.close()