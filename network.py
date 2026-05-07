from emoji_kitchen_api import EmojiKitchenAPI

class Network:

    def __init__(self, emoji_kitchen_api=None):
        self.pool_1 = []
        self.pool_2 = []
        self.emoji_kitchen_api = emoji_kitchen_api or EmojiKitchenAPI()

    def get_pool_1(self):
        self.pool_1 = ["😀", "😂", "😍", "🤔", "😎", "😭", "🎉", "👍", "👎", "🎉","😀", "😂", "🥰", "😎", "🤔", "😭", "😡"]
        return self.pool_1
    
    def get_pool_2(self):
        self.pool_2 = ["😀", "😂", "😍", "🤔", "😎", "😭", "😡", "👍", "👎", "😡","🍕", "🚗", "🔥", "✨", "❤️", "🍔", "⚽"]
        return self.pool_2
    
    def get_result(self, emoji_1, emoji_2, line_number):
               
        result_emoji_image = self.emoji_kitchen_api.get_emoji_image(emoji_1, emoji_2)
        if result_emoji_image:
            return result_emoji_image

        

