from diaries.DiarySample import DiarySample
from diaries.AtsushiDiary import AtshushiDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
           AtshushiDiary(),
] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
