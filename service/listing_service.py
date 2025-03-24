from persistence.listing_repository import ListingRepository
from persistence.user_repository import UserRepository
from persistence.category_repository import CategoryRepository

class ListingService:
    @staticmethod
    def create_listing(username, title, description, price, category):
        if not UserRepository.get_user(username):
            return {"Error - unknown user"}
        CategoryRepository.get_or_create_category(category)
        return ListingRepository.add_listing(username, title, description, price, category)

    @staticmethod
    def get_all_listings():
        return ListingService.get_all_listings()

    @staticmethod
    def get_listing(username, listing_id):
        """GET_LISTING：使用者驗證後，查詢某筆 listing 並以 to_string() 格式輸出"""
        if not UserRepository.get_user(username):
            return "Error - unknown user"
        
        listing = ListingRepository.get_listing_by_id(listing_id)
        if not listing:
            return "Error - not found"
        
        return listing.to_string()

    @staticmethod
    def delete_listing(username, listing_id):
        listings = ListingRepository.get_all_listings()
        listing = next((l for l in listings if l.id == listing_id), None)
        if not listing:
            return "Error - listing does not exist"
        if listing.username != username:
            return "Error - listing owner mismatch"
        ListingRepository.delete_listing(listing_id)
        return "Success"
