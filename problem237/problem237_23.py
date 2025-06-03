import numpy as np

N = int(input())
X = np.zeros([N,4], dtype=int)

for i in range(N):
    X[i,0], X[i,1] = map(int, input().split())
    X[i,2], X[i,3] = X[i,0] - X[i,1], X[i,0] + X[i,1]    

col_num = 3
X = X[np.argsort(X[:, col_num])]
cnt = 1
r_min = X[0,3]
for i in range(1,N):
    if X[i,2] >= r_min:
        cnt += 1
        r_min = X[i,3]
print(cnt)