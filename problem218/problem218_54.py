from collections import Counter
n = int(input())
s = [input() for i in range(n)]
num = Counter(s)
mx = max(num.values())
for i in sorted(num):
    if num[i] == mx:
        print(i)