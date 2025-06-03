from collections import deque
H,W = map(int,input().split())
A = [input().strip() for _ in range(H)]
d = 0
if A[0][0]=="#":
    d += 1
que = deque([(0,0,d)])
hist = [[H*W for _ in range(W)] for _ in range(H)]
hist[0][0] = d
while que:
    i,j,d = que.popleft()
    if j+1<W and A[i][j+1]==A[i][j]:
        if hist[i][j+1]>d:
            hist[i][j+1] = d
            que.append((i,j+1,d))
    elif j+1<W and A[i][j+1]!=A[i][j]:
        if hist[i][j+1]>d+1:
            hist[i][j+1] = d+1
            que.append((i,j+1,d+1))
    if i+1<H and A[i+1][j]==A[i][j]:
        if hist[i+1][j]>d:
            hist[i+1][j] = d
            que.append((i+1,j,d))
    elif i+1<H and A[i+1][j]!=A[i][j]:
        if hist[i+1][j]>d+1:
            hist[i+1][j] = d+1
            que.append((i+1,j,d+1))
m = hist[H-1][W-1]
print((m+1)//2)