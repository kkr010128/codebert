import sys
input = sys.stdin.readline
import numpy as np
from scipy.sparse.csgraph import floyd_warshall

n,m,l=map(int,input().split())
ans=[[0]*n for i in range(n)]
for i in range(m):
    a,b,c=[int(j) for j in input().split()]
    ans[a-1][b-1]=c
    ans[b-1][a-1]=c
q=int(input())
st=[]
for i in range(q):
    st.append([int(j)-1 for j in input().split()])

ans=floyd_warshall(ans)

for i in range(n):
    for j in range(n):
        if ans[i][j]<=l:
            ans[i][j]=1
        else:
            ans[i][j]=0

ans=floyd_warshall(ans)

for i,j in st:
    if ans[i][j]==float("inf"):
        print(-1)
    else:
        print(int(ans[i][j])-1)

