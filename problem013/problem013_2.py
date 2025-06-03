n = int(input())

mn = int(input())
ans = -1 * 10 ** 10
for i in range(n - 1):
    r = int(input())
    diff = r - mn
    if diff > ans:
        ans = diff
    mn = min(mn, r)

print(ans)

