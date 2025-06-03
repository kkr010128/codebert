n, m = map(int, input().split())
if n%2 == 1:
    a = 1
    b = n+1
    ans = []
    for i in range(m):
        a += 1
        b -= 1
        ans.append((a, b))
else:
    a = 1
    b = n+1
    S = set()
    ans = []
    for i in range(m):
        a += 1
        b -= 1
        r = min(b-a, n-(b-a))
        if r in S or r == n//2:
            b -= 1
            r = min(b-a, n-(b-a))
        ans.append((a, b))
        S.add(r)
for i in range(m):
    print(*ans[i])
