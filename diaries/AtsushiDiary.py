from diaries.AbstractDiary import AbstractDiary

class AtshushiDiary(AbstractDiary):
    def get_date(self):
        return "2024-11-28"
    
    def get_summary(self):
        return """GitHubの使い方が多くて大変だと感じた。"""
    
    def get_author(self):
        return "Atshushi"