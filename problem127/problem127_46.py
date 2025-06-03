x, y = [int(x) for x in input().split()]

flg = False
for c in range(x+1):
    t = x-c
    flg |= y == (2 * c + 4 * t)

print("Yes" if flg else "No")

