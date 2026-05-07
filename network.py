from emoji_kitchen_api import EmojiKitchenAPI
from emoji_combination_api import EmojiCombinationAPI

class Network:

    def __init__(self, emoji_kitchen_api=None, emoji_combination_api=None):
        self.emoji_kitchen_api = emoji_kitchen_api or EmojiKitchenAPI()
        self.emoji_combination_api = emoji_combination_api or EmojiCombinationAPI()

        self.pool_1 = self.emoji_combination_api.get_all_emojis()
        self.pool_2 = self.emoji_combination_api.get_all_emojis()

    def get_pool_1(self):
        return self.pool_1
    
    def get_pool_2(self):
        return self.pool_2
    
    def emoji_change(self, emoji_1, emoji_2, line_number):
        if line_number == 1 and emoji_1:
                self.pool_2 = self.emoji_combination_api.get_compatible_emojis(emoji_1)
            
        elif line_number == 2 and emoji_2:
                self.pool_1 = self.emoji_combination_api.get_compatible_emojis(emoji_2)
        else:
            return None

        if emoji_1 and emoji_2:

            result_emoji_image = self.emoji_kitchen_api.get_emoji_image(emoji_1, emoji_2)
            if result_emoji_image:
                return result_emoji_image
        else:
            return None

