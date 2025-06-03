import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = input().rstrip()
A = [0]*N
cnt = 0
S = reversed(S)
for i, s in enumerate(S):
    if s=="1":
        cnt += 1
        A[i] = cnt
    else:
        cnt = 0
dp = 0
res = []
while dp+M <= N-1:
    t = M - A[dp+M]
    if t>0:
        dp += t
    else:
        print(-1)
        exit()
    res.append(t)
res.append(N-dp)
res.reverse()
print(*res)