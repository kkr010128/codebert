from collections import Counter, defaultdict
# n = int(input())
# li = list(map(int, input().split()))
# n = int(input())
a, b = map(int, input().split())
d = defaultdict(lambda: 0)
d[1] = 300000
d[2] = 200000
d[3] = 100000
ans = d[a] + d[b]
if a == 1 and b == 1:
	ans += 400000
print(ans)
