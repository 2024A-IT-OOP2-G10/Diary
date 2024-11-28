from diaries.AbstractDiary import AbstractDiary

class YoshidaDiary(AbstractDiary):

    def get_date(self):
        return "2021-11-28"

    def get_summary(self):
        return """昨日は物理実験のレポートと、情報システム概論のレポートととにかく色々やった。
提出が近づいてきてから着手するのではなくて、もっと早めから行っておけばいいと思った。"""

    def get_author(self):
        return "Yoshida"
