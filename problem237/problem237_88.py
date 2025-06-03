import sys
input = sys.stdin.readline

N = int(input())
imo = []
xlmin = 0
xlmax = 0
for _ in range(N):
    x,l = map(int,input().split())
    imo.append([x-l,x+l-1])
imo = sorted(imo,key = lambda x: x[1])
cnt = 1
ls = imo[0][1]
for i in range(1,N):
    if imo[i][0]<=ls:
        continue
    else:
        cnt += 1
        ls = imo[i][1]
print(cnt)
