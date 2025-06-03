from collections import defaultdict
n = int(input())
a = [0]
a.extend(map(int, input().split()))
mp = defaultdict(int)
ans = 0
for i in range(1, n+1):
    ans += mp[i-a[i]]
    mp[i+a[i]] += 1
print(ans)