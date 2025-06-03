R,C,K= map(int,input().split(" "))
original=[[0]*(C+1) for i in range(R+1)]
for _ in range(K):
    r,c,v= map(int,input().split(" "))
    original[r][c]=v
d1=[[0]*(C+1) for i in range(R+1)]
d2=[[0]*(C+1) for i in range(R+1)]
d3=[[0]*(C+1) for i in range(R+1)]
for i in range(1,R+1):
    for j in range(1,C+1):
        curr= original[i][j]
        d1[i][j]=max(d1[i-1][j]+curr,d2[i-1][j]+curr,d3[i-1][j]+curr,d1[i][j-1],curr)
        d2[i][j]=max(d2[i][j-1],d1[i][j-1]+curr)
        d3[i][j]=max(d3[i][j-1],d2[i][j-1]+curr)
print(max(d1[-1][-1],d2[-1][-1],d3[-1][-1]))