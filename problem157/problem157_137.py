from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
dd = defaultdict(int)
ans = 0
for i, num in enumerate(a, start = 1):
    dd[i + num] += 1
for i, num in enumerate(a, start = 1):
    ans += dd[i - num]
print(ans)