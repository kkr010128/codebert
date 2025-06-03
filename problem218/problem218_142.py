from collections import Counter

n = int(input())
s = [input() for _ in range(n)]
cnt = Counter(s)
li = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))
m = li[0][1]
for i in range(len(li)):
    if li[i][1] < m:
        break
    print(li[i][0])
