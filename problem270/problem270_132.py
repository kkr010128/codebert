import sys
input = sys.stdin.readline

'''

'''

s = input().rstrip()

if s == "MON": print(6)
elif s == "SAT": print(1)
elif s == "FRI": print(2)
elif s == "THU": print(3)
elif s == "WED": print(4)
elif s == "TUE": print(5)
else:
    print(7)