from collections import defaultdict

n = int(input())
alst = list(map(int, input().split()))
ans = 0
dd = defaultdict(int)
for a in alst:
    dd[a] += 1
for _, num in dd.items():
    ans += num * (num - 1) // 2
for a in alst:
    num = dd[a]
    ret = ans - num * (num - 1) // 2 + (num - 1) * (num - 2) // 2
    print(ret)