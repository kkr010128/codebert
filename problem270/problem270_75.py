w = "SUN,MON,TUE,WED,THU,FRI,SAT".split(",")

S = input().strip()

for i, d in enumerate(w):
    if d == S:
        print(7 - i)

