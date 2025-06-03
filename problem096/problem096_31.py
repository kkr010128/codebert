n, d = map(int, input().split())
d_t = d**2
r = 0
for i in range(n):
    a, b = map(int, input().split())
    if d_t >= a**2 + b**2:
        r += 1
print(r)