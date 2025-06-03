import math
def koch(left, right, n):
    if n < 1: print(" ".join(map(str, left))); return
    
    s, t, u = [0] * 2, [0] * 2, [0] * 2
    s[0] = (2 * left[0] + right[0]) / 3.0
    s[1] = (2 * left[1] + right[1]) / 3.0
    
    t[0] = (left[0] + 2 * right[0]) / 3.0
    t[1] = (left[1] + 2 * right[1]) / 3.0
    
    u[0] = (t[0] - s[0]) * math.cos(math.pi/3) - (t[1] - s[1]) * math.sin(math.pi/3) + s[0]
    u[1] = (t[0] - s[0]) * math.sin(math.pi/3) + (t[1] - s[1]) * math.cos(math.pi/3) + s[1]
    
    koch(left, s, n-1)
    koch(s, u, n-1)
    koch(u, t, n-1)
    koch(t, right, n-1)
    
n = int(input())
left = [0, 0]
right = [100, 0]

koch(left, right, n)
print(right[0], right[1])
