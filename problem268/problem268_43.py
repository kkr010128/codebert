import sys,queue,math,copy
input = sys.stdin.readline
MOD = 10**9 + 7
LI = lambda : [int(x) for x in input().split()]
N = int(input())
A = LI()
c =[0,0,0]
cnt = [0 for _ in range(N)]
for i in range(N):
    cnt[i] = c.count(A[i])
    if cnt[i] == 0: break
    c[c.index(A[i])] += 1
ans = 1
for i in range(N):
    ans = (ans * cnt[i]) % MOD
print (ans)