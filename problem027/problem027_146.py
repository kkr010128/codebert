import math

n = int(input())
a = [0, 0]
b = [100, 0]
root3 = math.sqrt(3)


def koch(a, b, n):
    if n == 1:
        s = [(a[0] * 2 + b[0]) / 3, (a[1] * 2 + b[1]) / 3]
        t = [(a[0] + b[0] * 2) / 3, (a[1] + b[1] * 2) / 3]
        u = [(s[0] + t[0] - root3 * t[1] + root3 * s[1]) / 2,
             (s[1] + t[1] + root3 * t[0] - root3 * s[0]) / 2]
        print(*s)
        print(*u)
        print(*t)
        print(*b)

    elif n > 1:
        s = [(a[0] * 2 + b[0]) / 3, (a[1] * 2 + b[1]) / 3]
        t = [(a[0] + b[0] * 2) / 3, (a[1] + b[1] * 2) / 3]
        u = [(s[0] + t[0] - root3 * t[1] + root3 * s[1]) / 2,
             (s[1] + t[1] + root3 * t[0] - root3 * s[0]) / 2]
        koch(a, s, n-1)
        koch(s, u, n-1)
        koch(u, t, n-1)
        koch(t, b, n-1)


print(*a)
koch(a, b, n)
if n == 0:
    print(*b)

