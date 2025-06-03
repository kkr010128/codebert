n, x, t = map(int,input().split())
a = (int)(n / x)
if n % x != 0:
    a += 1
print(a * t)