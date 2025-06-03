n, t = map(int, input().split())
lst = [0 for _ in range(t)]
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort()
ans = 0
for a, b in ab:
    ans = max(ans, lst[-1] + b)
    for i in range(t - 1, a - 1, -1):
        lst[i] = max(lst[i], lst[i - a] + b)

print(ans)