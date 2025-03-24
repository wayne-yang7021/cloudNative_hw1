from persistence.listing_repository import ListingRepository
from persistence.user_repository import UserRepository

class CategoryService:
    @staticmethod
    def get_category_listings(username, category):
        """取得該分類下所有 listing，按 created_at 由新到舊排序"""
        if not UserRepository.get_user(username):
            return "Error - unknown user"

        listings = ListingRepository.get_all_listings()

        listings = listings[1:]
        
        # 過濾出該分類的 listing
        filtered = [
            listing for listing in listings 
            if listing.category.lower() == category.lower()
        ]

        if not filtered:
            return "Error - category not found"

        # 排序：created_at 由新到舊（時間字串倒序）
        filtered.sort(key=lambda l: l.created_at, reverse=True)

        # 回傳格式：<title>|<description>|<price>|<created_at>
        result_lines = [
            f"{l.title}|{l.description}|{l.price}|{l.created_at}|{category}|{l.username}" for l in filtered
        ]
        return "\n".join(result_lines)
    
    @staticmethod
    def get_top_category(username):
        """返回擁有最多 listing 的分類，若有多個則按字母排序"""
        if not UserRepository.get_user(username):
            return "Error - unknown user"

        category_counts = {}
        listings = ListingRepository.get_all_listings()

        for listing in listings:
            category_counts[listing.category] = category_counts.get(listing.category, 0) + 1

        if not category_counts:
            return "Error - no categories found"

        max_count = max(category_counts.values())

        # 找出所有符合最大數量的分類，並按字母排序
        top_categories = sorted([category for category, count in category_counts.items() if count == max_count])
        
        return ' '.join(top_categories)  # 返回字母順序第一的分類
