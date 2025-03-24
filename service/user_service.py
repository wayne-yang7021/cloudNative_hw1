from persistence.user_repository import UserRepository

class UserService:
    @staticmethod
    def register_user(username):
        if UserRepository.get_user(username):
            return "Error - user already existing"
        return UserRepository.add_user(username)
