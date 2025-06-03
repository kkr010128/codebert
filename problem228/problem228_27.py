from math import floor

H = int(input())

ans = 0
r = H
n = 0
while not (r == 1):
    n += 1
    ans += 2 ** n
    r = floor(r / 2)

ans += 1

print(ans)
