from diaries.DiarySample import DiarySample
from diaries.K23141_Diary import K23141_Diary
from diaries.k23111_diary import k23111_diary
from diaries.AtsushiDiary import AtshushiDiary
from diaries.YoshidaDiary import YoshidaDiary
from diaries.NishioDiary import NishioDiary 

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    k23111_diary(),
    YoshidaDiary(),
    NishioDiary(),
    AtshushiDiary(),
    K23141_Diary(),
    k23111_diary(),
] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
