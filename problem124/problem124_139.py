def main():
    from sys import setrecursionlimit, stdin, stderr
    from os import environ
    from collections import defaultdict, deque, Counter
    from math import ceil, floor
    from itertools import accumulate, combinations, combinations_with_replacement
    setrecursionlimit(10**6)
    dbg = (lambda *something: stderr.write("\033[92m{}\033[0m".format(str(something)+'\n'))) if 'TERM_PROGRAM' in environ else lambda *x: 0
    input = lambda: stdin.readline().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    P = 10**9+7
    INF = 10**18+10
    K = II()
    S = input()
    N = len(S)
    def gencmb(n,k):
        # N-1+K C K  ... N-1 C 0
        ans = [1]*(k+1)
        for i in range(1,k+1):
            ans[-i-1] = ans[-i] * (N+i-1) * pow(i,P-2,P) % P
        return ans
    ans = 0
    pow26 = [0] * (K+1)
    pow26[0] = 1
    for i in range(1,K+1):
        pow26[i] = pow26[i-1] * 26 % P
    pow25 = [0] * (K+1)
    pow25[0] = 1
    for i in range(1,K+1):
        pow25[i] = pow25[i-1] * 25 % P
    cmb = gencmb(N,K)
    for t in range(K+1):
        ans += pow26[t]*pow25[K-t]*cmb[t]%P
        ans %= P
    print(ans)

    
main()