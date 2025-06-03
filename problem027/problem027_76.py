from math import *
def koch(n, a, b):
    if n == 0:
        return
    th = pi * 60.0 / 180.0
    s = complex((2.0 * a.real + 1.0 * b.real) / 3.0, (2.0 * a.imag + 1.0 * b.imag) / 3.0)
    t = complex((1.0 * a.real + 2.0 * b.real) / 3.0, (1.0 * a.imag + 2.0 * b.imag) / 3.0)
    u = complex((t.real - s.real) * cos(th) - (t.imag - s.imag) * sin(th) + s.real,
                (t.real - s.real) * sin(th) + (t.imag - s.imag) * cos(th) + s.imag)
    koch(n - 1, a, s)
    print(s.real, s.imag)
    koch(n - 1, s, u)
    print(u.real, u.imag)
    koch(n - 1, u, t)
    print(t.real, t.imag)
    koch(n - 1, t, b)
n = int(input())
a = complex(0, 0)
b = complex(100, 0)
print(a.real, a.imag)
koch(n, a, b)
print(b.real, b.imag)

