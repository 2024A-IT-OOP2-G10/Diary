from diaries.K23141_Diary import K23141_Diary
from diaries.DiarySample import DiarySample

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), K23141_Diary(), ] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
