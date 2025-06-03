import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


N,K,S = MI()
if S == 10**9:
    ANS = [10**9]*K + [1]*(N-K)
else:
    ANS = [S]*K + [10**9]*(N-K)

print(*ANS)
