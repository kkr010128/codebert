s = input()
week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
for i in range(6):
    if s == week[i]:
        print(6 - i)
if s == "SUN":
    print("7")
