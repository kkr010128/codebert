import math

N = int(input()) 
A = list(map(int,input().split()))

up = [[] for _ in range(N+1)] # 葉から考慮した場合の、最小値
up[N] = [A[N],A[N]]
#print(up)
for i in reversed(range(N)):
    Min, Max = up[i+1]
    #print(Min,Max)
    Min_n = math.ceil(Min/2) + A[i]
    Max_n = Max + A[i]
    #print(A[i],i)
    up[i] = [Min_n, Max_n]
#print(up)

if up[0][0] >= 2:
    print(-1)
else:
    down = 1
    #print(down)
    ans = 1
    for i in range(1, N+1):
        down *= 2
        down = min(down,up[i][1]) - A[i]
        ans += down + A[i]
    print(ans)