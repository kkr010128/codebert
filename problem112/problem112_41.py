def sgn(x):
    if x>0:
        return 1
    elif x<0:
        return -1
    else:
        return 0
N,K=map(int,input().split())
A=[int(i) for i in input().split()]
mod=10**9+7
if K==N:
    ans=1
    for i in range(N):
        ans=ans*A[i]
        ans%=mod
    print(ans)
    exit()
if max(A)<0 and K%2==1:
    ans=1
    A.sort()
    for i in range(K):
        ans=ans*A[-i-1]
        ans%=mod
    print(ans)
    exit()
A.sort(key=lambda x:abs(x),reverse=True)
P=1
Pfugou=1
for i in range(K):
    P=P*A[i]
    P%=mod
    Pfugou=Pfugou*sgn(A[i])
if Pfugou!=-1:
    print(P)
    exit()
X=[]
Y=[]
for i in range(N):
    if A[i]>=0:
        X.append(A[i])
    else:
        Y.append(-A[i])
X.sort()
Y.sort()
S=[]
while(len(S)<K):
    if len(S)==K-1:
        S.append(X[-1])
        X.pop()
    elif len(X)<=1 and len(Y)<=1:
        #選んでないのが2個以下
        #len(S)<K<=N-1
        #len(S)=N-len(X)-len(Y)>=N-2
        #よってlen(S)=N-2,K=N-1
        #前述で処理済み
        #なのでここでやることはない
        pass
    elif len(X)<=1:
        S.append(Y[-1])
        S.append(Y[-2])
        Y.pop()
        Y.pop()
    elif len(Y)<=1:
        S.append(X[-1])
        S.append(X[-2])
        X.pop()
        X.pop()
    else:
        if X[-1]*X[-2]>Y[-1]*Y[-2]:
            S.append(X[-1])
            X.pop()
        else:
            S.append(Y[-1])
            S.append(Y[-2])
            Y.pop()
            Y.pop()
ans=1
for i in S:
    ans=ans*i
    ans%=mod
print(ans)