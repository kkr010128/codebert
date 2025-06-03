def main():
    from sys import setrecursionlimit, stdin
    from os import environ
    from collections import defaultdict, deque, Counter
    from math import ceil, floor, gcd
    from itertools import accumulate, combinations, combinations_with_replacement
    setrecursionlimit(10**6)
    dbg = (lambda *something: print(*something)) if 'TERM_PROGRAM' in environ else lambda *x: 0
    input = lambda: stdin.readline().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    P = 10**9+7
    INF = 10**9+10

    N = II()
    args = defaultdict(lambda:defaultdict(lambda:[0]*2))
    zeros = 0
    for _ in range(N):
        x,y = map(int,input().split())
        if x == 0:
            if y == 0:
                zeros += 1
            else:
                args[0][0][0] += 1
            continue
        elif y == 0:
            args[0][0][1] += 1
            continue
        
        g = gcd(x,y)
        x2,y2 = abs(x//g),abs(y//g)
        if x*y < 0:
            args[x2][y2][1] += 1
        else:
            args[y2][x2][0] += 1

    ans = 1
    for y, a in args.items():
        for x, p in a.items():
            ans *= (pow(2,p[0],P) + pow(2,p[1],P) -1)
            ans %= P
    print((ans + zeros -1 + P)%P)

main()