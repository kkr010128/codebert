days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
S = input()
if S == "SUN":
    print(7)
else:
    print(days.index("SUN") - days.index(S))
