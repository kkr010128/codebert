a, b, n = map(int, input().split())

if n <= b - 1:
    x = n
else:
    x = n - (n%b + 1)

ans = a*x//b - a*(x//b)
print(ans)