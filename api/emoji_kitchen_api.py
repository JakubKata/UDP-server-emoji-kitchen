import requests
import os
from requests.exceptions import RequestException
from dotenv import load_dotenv

BASE_URL = "https://tenor.googleapis.com/v2/featured"
CLIENT_KEY = "emoji_kitchen_funbox"

class EmojiKitchenAPI:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("API_KEY")
        

    def fetch_emoji_data(self, emoji_1, emoji_2) -> dict:
        payload = {
            "client_key": CLIENT_KEY,
            "q": f"{emoji_1}_{emoji_2}",
            "collection": "emoji_kitchen_v6",
            "key": self.api_key
        }

        try:           
            response = requests.get(BASE_URL, params = payload, timeout = 10)
            
            if response.status_code == 200:
                return response.json()
            else:
                return {}
        except RequestException as e:
            return {}

    def parse_emoji_url(self, raw_data) -> str | None:
        try:
            return raw_data.get("results", [])[0].get("url", "")
        except:
            return None

    def get_kitchen_combination(self, emoji_1, emoji_2) -> str | None:
        
        raw_data = self.fetch_emoji_data(emoji_1, emoji_2)
        if raw_data:
            return self.parse_emoji_url(raw_data)
        return None
    
    def download_emoji_image(self, url) -> bytes | None:
        try:
            response = requests.get(url, timeout = 10)
            if response.status_code == 200:
                return response.content
            else:
                return None
        except RequestException as e:
            return None
        
    def get_emoji_image(self, emoji_1, emoji_2) -> bytes | None:
        result_url = self.get_kitchen_combination(emoji_1, emoji_2)
        if result_url:
            return self.download_emoji_image(result_url)
        return None