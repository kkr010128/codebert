#E_Picking Goods
R,C,K = map(int,input().split())
A =     [[0  for j in range(C)] for i in range(R)]
varr = [[[0  for j in range(C)] for i in range(R)] for k in range(4)]

for inputk in range(K):
    r,c,v = map(int,input().split())
    A[r-1][c-1] = v

for i in range(R):  
    for j in range(C):
        for k in range(2,-1,-1):
            if varr[k][i][j] >= 0:
                if  varr[k+1][i][j] < varr[k][i][j] + A[i][j]:
                    varr[k+1][i][j] = varr[k][i][j] + A[i][j]
        for kk in range(0,4):
            if varr[kk][i][j] >= 0:
                if i +1 < R :
                    if  varr[0][i + 1][j] < varr[kk][i][j]:
                        varr[0][i + 1][j] = varr[kk][i][j] 
                if j +1 < C :
                    if  varr[kk][i][j + 1] < varr[kk][i][j]:
                        varr[kk][i][j + 1] = varr[kk][i][j] 
ans = 0
for k in range (4):
    if ans < varr[k][R-1][C-1]:
        ans = varr[k][R-1][C-1]

print(ans)
