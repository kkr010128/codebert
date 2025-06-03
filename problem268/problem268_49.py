import sys,queue,math,copy
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
INF = 10**18
MOD = 10**9 + 7
LI = lambda : [int(x) for x in input().split()]
_LI = lambda : [int(x)-1 for x in input().split()]
N = int(input())
A = LI()


c =[0,0,0]
cnt = [0 for _ in range(N)]
for i in range(N):
    cnt[i] = c.count(A[i])
    if cnt[i] == 0:
        print (0)
        exit (0)
    for j in range(3):
        if c[j] == A[i]:
            c[j] += 1
            break
ans = 1
for i in range(N):
    ans = (ans * cnt[i]) % MOD
print (ans)