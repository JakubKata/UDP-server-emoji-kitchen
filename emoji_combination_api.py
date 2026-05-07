import requests
from requests.exceptions import RequestException
from google.protobuf.json_format import MessageToDict

import schema_pb2

PARAMETER_URL = "https://www.google.com/logos/fnbx/emoji_kitchen/emoji_kitchen_pairs.11.pb"

class EmojiCombinationAPI:
    def __init__(self):
            self.emoji_to_id_map = {}
            self.id_to_emoji_map = {}

    def fetch_parameters(self) -> dict:
        try:
            response = requests.get(PARAMETER_URL, timeout=10)
            if response.status_code == 200:
                response_data = schema_pb2.EmojiKitchenData()
                response_data.ParseFromString(response.content) 
                return MessageToDict(response_data)
            else:
                return {}
        except RequestException as e:
            return {}
        except Exception as e:
            return {}

    def parse_emoji_id(self, raw_data) -> dict:
        try:
            emoji_list = raw_data.get("emojis", [])

            for emoji in emoji_list:
                emoji_id = emoji.get("id")
                emoji_char = emoji.get("emoji")

                if emoji_id is not None and emoji_char is not None:
                    self.emoji_to_id_map[emoji_char] = emoji_id
                    self.id_to_emoji_map[emoji_id] = emoji_char
            return 
        except:
            return {}
        
    def get_all_emojis(self) -> list:
        raw_data = self.fetch_parameters()
        if raw_data:
            self.parse_emoji_id(raw_data)
            return list(self.emoji_to_id_map.keys())
        return []
        
    def emoji_to_id(self, emoji) -> int | None:
        return self.emoji_to_id_map.get(emoji)

    def id_to_emoji(self, id) -> str | None:
        return self.id_to_emoji_map.get(id)
    
    def parse_combinations(self, raw_data) -> dict:
        try:
            combinations = raw_data.get("combinations", [])
            result = {}
            for combo in combinations:
                emoji_id = combo.get("id")
                compatibility_emoji_ids = combo.get("emojiIds" , [])
                
                if emoji_id is not None:
                    result[emoji_id] = compatibility_emoji_ids
            return result
        except:
            return {}
        
    def get_compatible_emojis(self, emoji) -> list:
        raw_data = self.fetch_parameters()
        if raw_data:
            combinations = self.parse_combinations(raw_data)
            emoji_id = self.emoji_to_id(emoji)
            compatible_ids = combinations.get(emoji_id, [])
            result = []
            for id in compatible_ids:
                result.append(self.id_to_emoji(id))
            return result
        return []
        
