n, x, t = map(int,input().split(' '))
r = int(n / x) + (1 if n % x > 0 else 0)
print(r * t)