week=["SUN","MON","TUE","WED","THU","FRI","SAT"]
s=input()
if s in week:
    x=week.index(s)
    print(7-x)