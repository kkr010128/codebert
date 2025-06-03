from collections import Counter
n, k = map(int, input().split())
a = [x - 1 for x in map(int, input().split())]

sa = [0 for _ in range(n+1)]
for i in range(n):
    sa[i+1] = (sa[i] + a[i]) % k
#print(sa)

if n < k:
    cnt = Counter(sa)
    ans = 0
    for x in cnt.values():
        ans += x * (x - 1) // 2
    print(ans)

else:
    cnt = Counter(sa[:k-1])
    ans = 0
    for i in range(n):
        cnt[sa[i]] -= 1
        if i + k - 1 <= n:
            cnt[sa[i+k-1]] += 1
        ans += cnt[sa[i]]
    print(ans)