a, b, n = map(int, input().split())

x = (n//b)*b - 1

if x == -1:
    x = n

ans = a*x//b - a*(x//b)
print(ans)