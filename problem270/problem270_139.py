import sys

youbi = ["MON", "TUE", "WED", "THU", "FRI", "SAT"]
S = input()

if S == "SUN":
    print(7)
    sys.exit()

for i, youbi in enumerate(youbi):
    if S == youbi:
        print(6-i)
