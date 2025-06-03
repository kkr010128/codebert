H,W,M=map(int,input().strip().split())
h=[0 for _ in range(H)]
w=[0 for _ in range(W)]

dp=[]
for m in range(M):
    i,j=map(int,input().strip().split())
    dp.append((i,j))
    h[i-1]+=1
    w[j-1]+=1

h_max=0
hmax_l=[]
for i in range(H):
    if h_max==h[i]:
        hmax_l.append(i+1)
    elif h_max<h[i]:
        h_max=h[i]
        hmax_l=[]
        hmax_l.append(i+1)
w_max=0
wmax_l=[]
for i in range(W):
    if w_max==w[i]:
        wmax_l.append(i+1)
    elif w_max<w[i]:
        w_max=w[i]
        wmax_l=[]
        wmax_l.append(i+1)

cnt=0
for m in range(M):
    if h[dp[m][0]-1]+w[dp[m][1]-1]==h_max+w_max:
        cnt+=1

ans=h_max+w_max if cnt<len(hmax_l)*len(wmax_l) else h_max+w_max-1
print(ans)