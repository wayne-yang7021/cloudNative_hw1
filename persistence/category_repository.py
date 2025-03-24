from persistence.database import get_connection

class CategoryRepository:
    @staticmethod
    def get_or_create_category(name):
        """檢查類別是否存在，若不存在則新增"""
        conn = get_connection()
        cursor = conn.cursor()
        
        # 查找是否已存在該分類
        cursor.execute("SELECT * FROM categories WHERE name = ?", (name,))
        category = cursor.fetchone()
        
        if not category:
            # 插入新分類
            cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
            conn.commit()
        
        conn.close()
