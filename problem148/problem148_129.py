a, b, c, k = map(int, input().split())
if k <= a:
    ans = k
elif k <= a + b:
    ans = a
else:
    ans = a * 2 + b - k  # a-(k-(a+b))
print(ans)