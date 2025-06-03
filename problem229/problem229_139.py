import sys,math,collections,itertools
input = sys.stdin.readline

H,N=list(map(int,input().split()))
AB = []
amax = 0
for _ in range(N):
    a,b=map(int,input().split())
    amax = max(amax,a)
    AB.append([a,b])
HN = [float('inf')]*(H+amax+1)
HN[0] = 0
for i in range(H+amax+1):
    for j in range(N):
        if AB[j][0]<=i:
            tmp = HN[i-AB[j][0]]+AB[j][1]
            HN[i] = min(HN[i],tmp)
        else:
            tmp = AB[j][1]
            HN[i] = min(HN[i],tmp)
print(min(HN[H:]))
