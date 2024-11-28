from diaries.AbstractDiary import AbstractDiary

class NishioDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return """今日の日記
    今日の天気は、晴れでした。
    今日の授業はあまりコードを書かなかったので、指が痛くなりませんでした。
    今日の夕食は、カレーにします。
    """

    def get_author(self):
        return "Nishio"
