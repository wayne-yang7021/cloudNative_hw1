class User:
    def __init__(self, username):
        self.username = username.lower()

class Listing:
    def __init__(self, username, title, description, price, category, created_at):
        self.username = username.lower()
        self.title = title
        self.description = description
        self.price = price
        self.category = category
        self.created_at = created_at

    def to_string(self):
        return f"{self.title}|{self.description}|{self.price}|{self.created_at}|{self.category}|{self.username}"

class Category:
    def __init__(self, title, description, price, created_at):
        self.title = title
        self.description = description
        self.price = price
        self.created_at = created_at

    def to_string(self):
        return f"{self.title}|{self.description}|{self.price}|{self.created_at}"
