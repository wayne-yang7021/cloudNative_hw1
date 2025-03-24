from persistence.database import get_connection
import sqlite3

class UserRepository:
    @staticmethod
    def add_user(username):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
            conn.commit()
            return "Success"
        except sqlite3.IntegrityError:
            return "Error - user already existing"
        finally:
            conn.close()

    @staticmethod
    def get_user(username):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()
        return user
