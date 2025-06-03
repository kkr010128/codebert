H,W=map(int,input().split())
s=[input()for _ in range(H)]
a=[[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if i==j==0:a[0][0]=0
        elif i==0:a[0][j]=a[0][j-1]if s[0][j]==s[0][j-1]else a[0][j-1]+1
        elif j==0:a[i][0]=a[i-1][0]if s[i][0]==s[i-1][0]else a[i-1][0]+1
        else:a[i][j]=min(a[i][j-1]if s[i][j]==s[i][j-1]else a[i][j-1]+1,a[i-1][j]if s[i][j]==s[i-1][j]else a[i-1][j]+1)
print((a[H-1][W-1]+1)//2 if s[0][0]=='.'else a[H-1][W-1]//2+1)
