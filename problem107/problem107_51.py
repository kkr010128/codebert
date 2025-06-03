N=int(input())
X=input()
popcount=X.count('1')
mod = [popcount+1, popcount-1]
bi = [[0] * N for _ in range(2)]
Xnum = [0] * 2
add_diff = [1, -1]
for j in range(2):
    if mod[j] != 0:
        for i in range(N):
            if i==0: bi[j][0]=1%mod[j]
            else: bi[j][i]=bi[j][i-1]*2%mod[j]
            Xnum[j] = (Xnum[j] + int(X[N-i-1])*bi[j][i])%mod[j]
for i in range(N):
    if popcount==1 and X[i]=='1':
        print(0)
        continue
    Xi = ( Xnum[int(X[i])] + add_diff[int(X[i])] * bi[int(X[i])][N-i-1] ) % mod[int(X[i])]
    ans = 1
    while Xi!=0:
        Xi = Xi % bin(Xi).count('1')
        ans += 1
    print(ans)