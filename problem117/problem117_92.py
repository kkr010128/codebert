import bisect
N,M,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
time = 0
cnt = 0
C = []
SA =[0]
SB =[0]
for a in A:
    SA.append(SA[-1] + a)
for b in B:
    SB.append(SB[-1] + b)
for x in range(N+1):
    L = K - SA[x]
    if L < 0:
        break
    y_max = bisect.bisect_right(SB, L) - 1

    C.append(y_max + x)
print(max(C))