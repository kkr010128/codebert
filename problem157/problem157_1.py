from collections import defaultdict
d = defaultdict(int)
N = int(input())
arr = list(map(int, input().split()))
ans = 0
for i in range(N):
    ans += d[i-arr[i]]
    d[i+arr[i]] += 1
print(ans)