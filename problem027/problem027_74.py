import math
n = int(input())
a = [0] * 2
b = [0] * 2
a[0] = 0
b[0] = 100

def koch(n, a, b):
    if n == 0:
        return
    
    s = [0] * 2
    t = [0] * 2
    u =[0] * 2
    
    s[0] = (2.0 * a[0] + 1.0 * b[0]) / 3.0
    s[1] = (2.0 * a[1] + 1.0 * b[1]) / 3.0
    t[0] = (1.0 * a[0] + 2.0 * b[0]) / 3.0
    t[1] = (1.0 * a[1] + 2.0 * b[1]) / 3.0
    u[0] = (t[0] - s[0]) * math.cos(math.pi/3) - (t[1] - s[1]) * math.sin(math.pi/3) + s[0]
    u[1] = (t[0] - s[0]) * math.sin(math.pi/3) + (t[1] - s[1]) * math.cos(math.pi/3) + s[1]
    
    koch(n - 1, a, s)
    print(s[0], s[1])
    koch(n - 1, s, u)
    print(u[0], u[1])
    koch(n - 1, u, t)
    print(t[0], t[1])
    koch(n - 1, t, b)

print(a[0], a[1])
koch(n, a, b)
print(b[0], b[1])
