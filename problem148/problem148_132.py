a, b, c, k = map(int, input().split())
ans = 0
if k < a:
    ans = 1 * k
elif k <= a + b:
    ans = 1 * a
elif k > a + b:
    ans = 1 * a - 1 * (k-a-b)
print(ans)