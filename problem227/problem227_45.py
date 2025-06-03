def solve():
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    s.sort(reverse=True)
    if k >= n:
        print(0)
        exit()
    else:
        print(sum(s[k:]))


solve()
