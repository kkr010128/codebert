n,k = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]
s = [0]
for i in range(len(a)):
    s.append(s[-1]+a[i])
for i in range(len(s)):
    s[i] = (s[i] - i) % k
# print(s)
d = {0:1}
ans = 0
for j in range(1,n+1):
    if s[j] in d:
        d[s[j]] += 1
    else:
        d[s[j]] = 1
    if j >= k:
        d[s[j-k]] -= 1
    ans += d[s[j]] - 1
    # print(d)
    # print(ans)
print(ans)