# ALDS1_5_C
import math

n = int(input())
def koch(d, p1, p2):
    if d == 0:
        return
    s = [(2 * p1[0] + p2[0]) / 3, (2 * p1[1] + p2[1]) / 3]
    t = [(p1[0] + 2 * p2[0]) / 3, (p1[1] + 2 * p2[1]) / 3]
    u = [(t[0] - s[0]) * 0.5 - (t[1] - s[1]) * 0.866025403 + s[0],
        (t[0] - s[0]) * 0.866025403 + (t[1] - s[1]) * 0.5 + s[1]]

    koch(d-1, p1, s)
    print(*s)
    koch(d-1, s, u)
    print(*u)
    koch(d-1, u, t)
    print(*t)
    koch(d-1, t, p2)

print(0.0, 0.0)
koch(n, [0, 0], [100, 0])
print(100.0, 0.0)
