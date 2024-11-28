from diaries.DiarySample import DiarySample
from diaries.k23065_diary import k23065_Diary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
           k23065_Diary, 
] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
