from hugchat import hugchat
from hugchat.login import Login
import time
import sys
class login:
    def __init__(self, email :str , pass_w: str):
        self.pass_w = pass_w
        self.email = email
    def login(self):
        sign = Login(self.email, self.pass_w)
        cookies = sign.login()
        cookie_path_dir = "./credentials"
        sign.saveCookiesToDir(cookie_path_dir)
        chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
        return chatbot
       
