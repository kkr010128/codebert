#3 Range Flip Find Route
h,w = map(int,input().split())
s= [None for i in range(h)]
for i in range(h):
    s[i] = input()
    
dp = [[0]*w for i in range(h)]

now=0
if s[0][0]=="#":
    now+=1
    dp[0][0]=now
for i in range(1,w):
    if s[0][i-1]=="." and s[0][i]=="#":
        now+=1
    dp[0][i]=now
        
now=0
if s[0][0]=="#":
    now+=1
for i in range(1,h):
    if s[i-1][0]=="." and s[i][0]=="#":
        now+=1
    dp[i][0]=now

for i in range(1,h):
    for j in range(1,w):
        cand1 = dp[i-1][j] + (s[i-1][j]=="." and s[i][j]=="#")
        cand2 = dp[i][j-1] + (s[i][j-1]=="." and s[i][j]=="#")
        dp[i][j]=min(cand1,cand2)
        
print(dp[-1][-1])