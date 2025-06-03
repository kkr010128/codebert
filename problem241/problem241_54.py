inf=float("inf")  


h,w=map(int,input().split())
s=[["#"]*(w+2) for i in range(h+2)]
for i in range(h):
    s[i+1]=["#"]+list(input())+["#"]

#h,w=3,5
#s=[['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '#', '.', '#'], ['#', '.', '#', '.', '#', '.', '#'], ['#', '.', '#', '.', '.', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']]    

nv=h*w
dp=[[inf]*nv for i in range(nv)] 

def nhw(hi,wi):
    return (hi-1)*w+wi-1

for i in range(1,h+1):
    for j in range(1,w+1):
        if s[i][j]=="#":
            continue
        vij=nhw(i,j)
        if s[i-1][j]==".":
            vij2=nhw(i-1,j)
            dp[vij][vij2]=1
            dp[vij2][vij]=1
        if s[i+1][j]==".":
            vij2=nhw(i+1,j)
            dp[vij][vij2]=1
            dp[vij2][vij]=1
        if s[i][j-1]==".":
            vij2=nhw(i,j-1)
            dp[vij][vij2]=1
            dp[vij2][vij]=1
        if s[i][j+1]==".":
            vij2=nhw(i,j+1)
            dp[vij][vij2]=1
            dp[vij2][vij]=1
for i in range(nv):
    dp[i][i]=0
           
#print(dp)
for k in range(nv):
    for i in range(nv):
        for j in range(nv):
            dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j])
#    print(dp)
#print(dp)
dpmax=0
for i in range(nv):
    for j in range(nv):
        if dp[i][j]!=inf:
            if dpmax<dp[i][j]:
                dpmax=dp[i][j]
print(dpmax)
