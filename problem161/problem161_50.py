a, b, n = map(int,input().split())

if n >= b:
    print(int(a - a / b))
else:
    print(int(a * n / b) - a * int(n / b))
