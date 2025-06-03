n = int(input())

ans = 0
for x in (int(input()) for _ in range(n)):
    flg = True
    for y in range(2, int(x**0.5+1)):
        if x % y == 0:
            flg = False
            break
    if flg:
        ans += 1

print(ans)