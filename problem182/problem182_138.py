n,k,c = map(int, input().split())
s = input()

# 計算途中はi=0~n-1日とする

# [a,b] i日までで、限界まで働くとa回働けてb日まで働けない
pre = [[0,0] for i in range(n)]
if s[0]=='o':
    pre[0]=[1,c]
    for j in range(c):
        if 1+j < n:
            pre[1+j] = pre[0] + []

for i in range(1,n):
    if pre[i]==[0,0]:
        if s[i]=='o':
            pre[i][0]=pre[i-1][0]+1
            pre[i][1]+=i+c
            for j in range(c):
                if i+j+1<n:
                    pre[i+j+1]=pre[i]+[]
        else:
            pre[i]=pre[i-1]+[]

# i日以降で限界まで働くとa回働ける
post = [0 for i in range(n)]
if s[-1]=='o':
    post[-1]=1
    for j in range(c):
        if 0 <= n-1-j-1 < n:
            post[-1-j-1] = post[-1]

for i in range(1,n):
    if post[n-i-1]==0:
        if s[n-i-1]=='o':
            post[n-i-1]=post[n-i]+1
            for j in range(c):
                if 0<=n-i-1-j-1<n:
                    post[n-i-1-j-1]=post[n-i-1]
        else:
            post[n-i-1]=post[n-i]

# 0日、n+1日を追加。iを1~n日にする
pre = [[0,0]]+pre+[[0,0]]
post = [0]+post+[0]

# i日に休んだときに、働く回数がkに到達するか調べる
ans = []
for i in range(1,n+1):
    if s[i-1]=='o':
        work, rest = pre[i-1]
        day = min(max(rest,i)+1,n+1)
        work = work + post[day]
        if work<k:
            ans.append(i)

for i in range(len(ans)):
    print(ans[i])