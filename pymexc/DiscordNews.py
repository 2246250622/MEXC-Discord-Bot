import requests

class DiscordNews:

    def __init__(self, webhook, username, avatar_url, feed):
        self.webhook = webhook
        self.username = username
        self.avatar_url = avatar_url
        self.feed = feed
        
    def prepare_and_notify(self):
        for entry in self.feed.entries:
            self.__notify_to_discord_channel(entry)
    
    def __notify_to_discord_channel(self, data):
        headers = { "Content-Type": "application/json" }
        description = f'''
        New Post: **{data.title}**
        
Autor: "BaBy仔"
{data.link}
        '''
        payload = {
            "username": self.username,
            "description": description,
            "avatar_url": self.avatar_url
        } 
        return requests.post(url=self.webhook, headers=headers, json=payload)