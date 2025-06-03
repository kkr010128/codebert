while True:
    n, x = map(int, raw_input().split())
    if (n, x) == (0, 0):
        break
    ans = 0
    for a in xrange(1, n+1):
        for b in xrange(a+1, n+1):
            for c in xrange(b+1, n+1):
                if a + b + c == x:
                    ans += 1
    print ans