from service.user_service import UserService
from service.listing_service import ListingService
from service.category_service import CategoryService
from typing import List
import re

class CommandProcessor:
    def __init__(self):
        self.commands = {
            "REGISTER": self.register,
            "CREATE_LISTING": self.create_listing,
            "GET_TOP_CATEGORY": self.get_top_category,
            "DELETE_LISTING": self.delete_listing,
            "GET_TOP_CATEGORY": self.get_top_category,
            "GET_CATEGORY": self.get_category_listings,
            "GET_LISTING": self.get_listing,
        }

    def parse_command(command_line: str) -> List[str]:
        """process command, deal with punctuation"""
        tokens = []
        current_token = ""
        in_quotes = False
        
        for char in command_line:
            if char == "'" and not in_quotes:
                in_quotes = True
            elif char == "'" and in_quotes:
                in_quotes = False
                tokens.append(current_token)
                current_token = ""
            elif char.isspace() and not in_quotes:
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
            else:
                current_token += char
        
        if current_token:
            tokens.append(current_token)
        
        return tokens

    # Process the commands and separate the arguments
    def process_command(self, command_line):
        pattern = r"'([^']*)'|(\S+)"
        matches = re.findall(pattern, command_line)

        # 將匹配結果組成 list，去除多餘的 tuple 格式
        tokens = [match[0] if match[0] else match[1] for match in matches]

        # 自動將數字轉換為 float 或 int
        parsed_tokens = [int(token) if token.replace('.', '', 1).isdigit() else token for token in tokens]
        if not parsed_tokens:
            return "Invalid command"
        
        command = parsed_tokens[0].upper()
        if command not in self.commands:
            return f"Unknown command: {command}"
        
        return self.commands[command](parsed_tokens[1:])

    def register(self, args):
        if len(args) != 1:
            return "Usage: REGISTER <username>"
        
        return UserService.register_user(args[0])

    def create_listing(self, args):
        if len(args) != 5:
            return "Usage: CREATE_LISTING <username> <title> <description> <price> <category>"
        return ListingService.create_listing(*args)
    
    def delete_listing(self, args):
        if len(args) != 2:
            return "Usage: DELETE_LISTING <username> <listing_id>"
        return ListingService.delete_listing(*args)
    
    def get_listing(self, args):
        if len(args) != 2:
            return "Usage: GET_LISTINGS <username> <listing_id>"
        return ListingService.get_listing(*args)
    
    def get_category_listings(self, args):
        if len(args) != 2:
            return "Usage: GET_CATEGORY <username> <category>"
        return CategoryService.get_category_listings(*args)

    def get_top_category(self, args):
        if len(args) != 1:
            return "Usage: GET_TOP_CATEGORY <username>"
        return CategoryService.get_top_category(*args)
    
   
    