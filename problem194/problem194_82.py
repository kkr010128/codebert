h, w  = map(int, input().split())
s = [input() for _ in range(h)]
m = [[-1]*w for _ in range(h)]
def dp(x, y):
    if m[x][y] == -1:
        if x == 0 and y == 0:
            m[x][y] = 1 if s[x][y] == "#" else 0
        elif x == 0:
            a = dp(x, y-1)
            m[x][y] = a+1 if s[x][y] == "#" and s[x][y-1] == "." else a
        elif y == 0:
            b = dp(x-1, y)
            m[x][y] = b+1 if s[x][y] == "#" and s[x-1][y] == "." else b
        else:
            a = dp(x, y-1)
            b = dp(x-1, y)
            c = a+1 if s[x][y] == "#" and s[x][y-1] == "." else a
            d = b+1 if s[x][y] == "#" and s[x-1][y] == "." else b
            m[x][y] = min(c, d)
    return m[x][y]
print(dp(h-1, w-1))