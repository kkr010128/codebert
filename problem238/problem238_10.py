n, k, s = map(int, input().split())

ans = [s for _ in range(k)]
if s == 10**9:
    others = [1 for _ in range(n-k)]
    ans = ans + others
    print(' '.join(map(str, ans)))
else:
    others = [10**9 for _ in range(n-k)]
    ans = ans + others
    print(' '.join(map(str, ans)))

