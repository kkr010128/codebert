days = ["DAYS","SAT","FRI","THU","WED","TUE","MON","SUN"]
s = str(input())
for i in days:
    if i == s:
        print(days.index(i))
        break