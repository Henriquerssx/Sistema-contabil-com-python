# app/user_dao.py
from app.database import get_db_connection
from app.criptografia_util import hash_password

class UserDAO:
    def add_user(self, usuario, senha):
        conn = get_db_connection()
        try:
            conn.execute(
                "INSERT INTO usuarios (usuario, senha_hash) VALUES (?, ?)",
                (usuario, hash_password(senha))
            )
            conn.commit()
            return True
        except conn.IntegrityError: # Usuário já existe
            return False
        finally:
            conn.close()

    def get_user(self, usuario):
        conn = get_db_connection()
        user = conn.execute("SELECT * FROM usuarios WHERE usuario = ?", (usuario,)).fetchone()
        conn.close()
        return user