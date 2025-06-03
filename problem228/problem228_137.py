N = int(input())

ans = 0
cnt = 1
while N > 0:
    if N == 1:
        ans += cnt
        break
    N //= 2
    ans += cnt
    cnt *= 2
print(ans)
