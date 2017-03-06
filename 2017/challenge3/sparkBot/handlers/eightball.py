from handler_base import MessageHandler
import json
import random


class Eightball(MessageHandler):
    
    def __init__(self, path_to_file="handlers/data_files/eightball.json"):
        with open(path_to_file) as json_file:
            self.data = json.load(json_file)
        pass      
    
    def handle_message(self, raw_msg, user_email, username):
        if str(raw_msg).lower() == "eightball":
            return random.choice(self.data["predictions"])
        return False

    def help(self):
        return "**eightball** - Get a prediction"
