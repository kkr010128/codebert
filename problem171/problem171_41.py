N=int(input())
A=list(map(int,input().split()))

L=[[10**10,0]]
for i in range(N):
    L.append([A[i],i])
L.sort(reverse=True)
#print(L)
DP=[[0 for i in range(N+1)]for j in range(N+1)]
#j=右に押し込んだ数
for i in range(1,N+1):
    for j in range(i+1):
        if j==0:
            DP[i][j]=DP[i-1][j]+L[i][0]*abs(L[i][1]-(i-1))
            #print(DP,DP[i-1][j]+L[i][0]*abs(L[i][1]-(i-1)))
        elif j==i:
            DP[i][j]=DP[i-1][j-1]+L[i][0]*abs(L[i][1]-(N-j))
            #print(DP,DP[i-1][j-1]+L[i][0]*abs(L[i][1]-(N-j)))
        else:
            DP[i][j]=max(DP[i-1][j]+L[i][0]*abs(L[i][1]-(i-1-j)),DP[i-1][j-1]+L[i][0]*abs(L[i][1]-(N-j)))
            #print(DP,DP[i-1][j]+L[i][0]*abs(L[i][1]-(i-1-j)),DP[i-1][j-1]+L[i][0]*abs(L[i][1]-(N-j)))
print(max(DP[-1]))