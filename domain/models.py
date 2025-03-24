from typing import List


class User:
    def __init__(self, username):
        self.username = username.lower()

class Listing:
    def __init__(self, id,  username, title, description, price, category, created_at):
        self.id = id
        self.username = username.lower()
        self.title = title
        self.description = description
        self.price = price
        self.category = category
        self.created_at = created_at

    def to_string(self):
        return f"{self.title}|{self.description}|{self.price}|{self.created_at}|{self.category}|{self.username}"

class Category:
    def __init__(self, name,):
        self.name = name
        self.listing_ids: List[int] = []
