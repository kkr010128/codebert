from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))
cnt = defaultdict(int)
ans = 0
for i, a in enumerate(A):
    ans += cnt[i+1 - a]
    cnt[i+1 + a] += 1
print(ans)