import math


def make_stu(p1, p2):
    s = [(2 * p1[0] + p2[0]) / 3, (2 * p1[1] + p2[1]) / 3]
    t = [(p1[0] + 2 * p2[0]) / 3, (p1[1] + 2 * p2[1]) / 3]
    u = [s[0] + (t[0] - s[0]) / 2 - math.sqrt(3) * (t[1] - s[1]) / 2,
         s[1] + (t[1] - s[1]) / 2 + math.sqrt(3) * (t[0] - s[0]) / 2]
    return s, t, u


def koch_curve(n, p1, p2):
    if n >= 1:
        s, t, u = make_stu(p1, p2)
        if n == 1:
            print(s[0], s[1])
            print(u[0], u[1])
            print(t[0], t[1])
        else:
            koch_curve(n - 1, p1, s)
            print(s[0], s[1])
            koch_curve(n - 1, s, u)
            print(u[0], u[1])
            koch_curve(n - 1, u, t)
            print(t[0], t[1])
            koch_curve(n - 1, t, p2)

n = int(input())

print(0.0, 0.0)
koch_curve(n, [0.0, 0.0], [100.0, 0.0])
print(100.0, 0.0)
