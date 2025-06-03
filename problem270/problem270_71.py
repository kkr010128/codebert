# A, Can'tWait for Holiday
# 今日の曜日を表す文字列Sが与えられます。
# Sは'SUN','MON','TUE','WED','THU','FRI','SAT'のいずれかであり、それぞれ日曜日、月曜日、火曜日。水曜日、木曜日、金曜日、土曜日を表します。
# 月の日曜日（あす以降）が何日後か求めてください。

# Sは'SUN','MON','TUE','WED','THU','FRI','SAT'のいずれか。

S = input()

if S == 'MON':
    print(6)
elif S == 'TUE':
    print(5)
elif S == 'WED':
    print(4)
elif S == 'THU':
    print(3)
elif S == 'FRI':
    print(2)
elif S == 'SAT':
    print(1)
else:print(7)