import collections

cnt = collections.defaultdict(int)
N = int(input())
ans = 0
height = list(map(int, input().split()))
for n in range(1, N+1):
    ans += cnt[n - height[n-1]]
    cnt[n+height[n-1]] += 1
print(ans)