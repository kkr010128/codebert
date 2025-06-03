import itertools
while True:
    n, x = map(int, input().split())
    if n == x == 0:
        break
    ans = 0
    for t in list(itertools.combinations([i + 1 for i in range(n)], 3)):
        if sum(t) == x:
            ans += 1
    print(ans)