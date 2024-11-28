from diaries.DiarySample import DiarySample
from diaries.k23111_diary import k23111_diary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(), 
    k23111_diary(),
] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
