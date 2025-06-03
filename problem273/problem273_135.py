n, k = map(int, input().split())
a = list(map(int, input().split()))

s = [0] * (n+1)

for i in range(n):
    s[i+1] = s[i] + a[i]
    s[i] = (s[i] - i) % k
s[n] = (s[n] - n) % k

count = dict()
for i in range(min(k-1, n+1)):
    if not s[i] in count:
        count[s[i]] = 0
    count[s[i]] += 1

ans = 0
for i in range(k-1, n+1):
    if not s[i] in count:
        count[s[i]] = 0
    count[s[i]] += 1
    count[s[i-k+1]] -= 1
    ans += count[s[i-k+1]]

for i in count.values():
    ans += i * (i - 1) // 2

print(ans)