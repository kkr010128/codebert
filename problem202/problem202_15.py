n, a, b = map(int, input().split())

ans = (n // (a+b)) * a
temp = n % (a+b)
if temp <= a:
    ans += temp
else:
    ans += a

print(ans)
