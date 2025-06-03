from collections import deque
H, W = map(int, input().split())
S_raw = [list(input()) for _ in range(H)]
m = 0
def calc(h,w):
    S = [list(S_raw[i][j] for j in range(W)) for i in range(H)]
    S[h][w]=0
    queue = deque([(h,w)])
    while queue:
        q = queue.popleft()
        for x in ((q[0]-1, q[1]),(q[0]+1, q[1]), (q[0], q[1]-1), (q[0], q[1]+1)):
          if 0<=x[0]<=H-1 and 0<=x[1]<=W-1:
            if S[x[0]][x[1]]==".":
              S[x[0]][x[1]] = S[q[0]][q[1]]+1
              queue.append(x)
    return max(S[h][w] for w in range(W) for h in range(H) \
                    if str(S[h][w]).isdigit())    
for h in range(H):
  for w in range(W):
    if S_raw[h][w]==".":
        m = max(m, calc(h,w))
print(m)