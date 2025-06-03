from collections import deque
import copy
H,W=map(int,input().split())
S=[list(input()) for _ in range(H)]
S1=copy.deepcopy(S)
ans=[]

sy=0
sx=0
for i in range(H):
    for j in range(W):
        c=0
        route=deque([(i,j,0)])
        S=copy.deepcopy(S1)
        while route:
            a,b,n=route.popleft()
            c=n
            if 0<=a<=H-1 and 0<=b<=W-1:
                if S[a][b]=='.':
                    S[a][b]='#'
                    route.append((a+1,b,n+1))
                    route.append((a-1,b,n+1))
                    route.append((a,b+1,n+1))
                    route.append((a,b-1,n+1))
                    
        ans.append(c-1)

print(max(ans))
