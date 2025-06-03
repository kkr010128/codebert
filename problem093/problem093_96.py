import sys
input = sys.stdin.readline

N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = -10**18

for i in range(N):
    now = i
    visit = [False]*N
    visit[now] = True
    l = []
    
    while True:
        nex = P[now]-1
        l.append(C[nex])
        
        if visit[nex]:
            break
        
        visit[nex] = True
        now = nex
    
    s = sum(l)
    acc = 0
    
    for j in range(min(K, len(l))):
        acc += l[j]
        ans = max(ans, acc+max(0, (K-j-1)//len(l)*s))

print(ans)