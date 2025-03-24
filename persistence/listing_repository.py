from persistence.database import get_connection
from domain.models import Listing
from datetime import datetime

class ListingRepository:
    @staticmethod
    def add_listing(username, title, description, price, category):
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO listings (username, title, description, price, category, created_at) 
            VALUES (?, ?, ?, ?, ?, ?)""",
            (username, title, description, price, category, created_at))
        conn.commit()
        listing_id = cursor.lastrowid
        conn.close()
        return listing_id
    
    @staticmethod
    def get_all_listings():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM listings")
        listings = cursor.fetchall()
        conn.close()
        return [Listing(*listing) for listing in listings]
    
    @staticmethod
    def get_listing_by_id(listing_id):
        """根據 listing_id 回傳該筆 listing（不檢查 username）"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM listings WHERE id = ?", (listing_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return Listing(*row)  # 排除 ID 欄位，因 Listing class 不需要 id
        else:
            return None
    
    @staticmethod
    def delete_listing(listing_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM listings WHERE id = ?", (listing_id,))
        conn.commit()
        conn.close()