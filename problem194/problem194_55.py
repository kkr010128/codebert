H,W=map(int,input().split())
s=[]
for _ in range(H):
    s.append(list(input()))

inf=float("inf")
ans=[[inf]*W for _ in range(H)]

if s[0][0]==".":
    ans[0][0]=0
else:
    ans[0][0]=1

for i in range(H):
    for j in range(W):
        if j!=W-1:
            if s[i][j]=="." and s[i][j+1]=="#":
                ans[i][j+1]=min(ans[i][j]+1,ans[i][j+1])
            else:
                ans[i][j+1]=min(ans[i][j],ans[i][j+1])
        if i!=H-1:
            if s[i][j]=="." and s[i+1][j]=="#":
                ans[i+1][j]=min(ans[i][j]+1,ans[i+1][j])
            else:
                ans[i+1][j]=min(ans[i][j],ans[i+1][j]) 

print(ans[H-1][W-1])
