from sys import stdin

lis = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
S = input()
k = 0
for i in range(7):
    if lis[i] == S:
        k = i
print(7 - k)
