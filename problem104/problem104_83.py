L, R, d = map(int,input().split())
ans = 0
while L <= R:
    if L % d == 0:
        ans += 1
    L += 1
print(ans)