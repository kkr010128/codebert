from sys import stdin

n = int(input())

xs = [int(input()) for _ in range(n)]

ans = 0
for x in xs:
    flg = True
    for y in range(2, int(x**0.5+1)):
        if x % y == 0:
            flg = False
            break
    if flg:
        ans += 1

print(ans)