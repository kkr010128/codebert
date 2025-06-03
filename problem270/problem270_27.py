days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
S = input()
for i in range(7):
    if S == days[i]:
        print(7 - i)
        exit()
