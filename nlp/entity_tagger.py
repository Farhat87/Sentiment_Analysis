import re

class EntityTagger:
    def __init__(self):
        # Example finance-related keywords (you can expand this)
        self.keywords = ['Tesla', 'Apple', 'Nifty', 'Sensex', 'Gold', 'Bitcoin']

    def tag_instruments(self, text):
        tags = []
        for keyword in self.keywords:
            if re.search(rf'\b{keyword}\b', text, re.IGNORECASE):
                tags.append(keyword)
        return tags