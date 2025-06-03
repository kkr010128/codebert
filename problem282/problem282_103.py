#ALL you can eat 
#0-1 なっぷサック問題をとく* N

#要領T-1のバックと　大きさがA,価値がBの荷物がNこずつある。　この時これらを使って価値をT-1をこえない範囲で最大にする方法を考える。


#dpl[N][V]=1番目からN番目までの荷物を用いて、重さをVにする上で実現可能な価値の最大値
N,T=map(int,input().split())
d=[]
for i in range(N):
    a,b=map(int,input().split())
    d.append((a,b))
dpl=[[0 for i in range(T)] for j in range(N+1)]
for i in range(N):
    weight,value=d[i]
    for j in range(T):
        if j>=weight:
            dpl[i+1][j]=max(dpl[i][j],dpl[i][j-weight]+value)
        else:
            dpl[i+1][j]=dpl[i][j]

            
#dpr[K][V]=K番目からN番目までの荷物を用いて、重さをVにする上で実現可能な価値の最大値
dpr=[[0 for i in range(T)] for j in range(N+2)]
for i in range(1,N+1):
    weight,value=d[-i]
    for j in range(T):
        if j>=weight:
            dpr[N+1-i][j]=max(dpr[N+2-i][j],dpr[N+2-i][j-weight]+value)
        else:
            dpr[N+1-i][j]=dpr[N+2-i][j]

#dpr[K][V]=K番目からN番目までの荷物を用いて重さをV以下にする上で実現可能な価値の最大値にする
for i in range(1,N+1):
    for j in range(1,T):
        dpr[i][j]=max(dpr[i][j],dpr[i][j-1])
    
ans=0
for i in range(N):
    sub=d[i][1]
    #i+1番目の物を使わない
    add=0
    for j in range(T):
        add=max(add,dpl[i][j]+dpr[i+2][T-1-j])
    sub+=add
    ans=max(sub,ans)
print(ans)