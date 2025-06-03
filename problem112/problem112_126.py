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
    multimul = lambda L,i=0: (L[i] * multimul(L,i+1) % P  if i+1 < len(L) else  L[i])
    INF = 10**18+10

    N,K = LMIIS()
    A = LMIIS()
    
    if N == K:
        print(multimul(A))
        return
    not_negative = []
    negative = []
    for a in A:
        if a < 0:
            negative.append(a)
        else:
            not_negative.append(a)
    if len(negative) == N and K % 2 == 1:
        print(multimul(sorted(negative,reverse=True)[:K]))
        return
    not_negative.sort(reverse=True)

    not_negative = deque(not_negative)
    negative.sort()
    negative = deque(negative)
    ans = 1
    num_multiplied = 0
    while num_multiplied < K:
        if num_multiplied == K-1 or len(negative) < 2 or len(not_negative) >= 2 and not_negative[0] * not_negative[1] > negative[0] * negative[1]:
            ans = ans * not_negative.popleft() % P
            num_multiplied += 1
        else:
            ans = ans * negative.popleft() * negative.popleft() % P
            num_multiplied += 2
    print(ans)
            


    
main()