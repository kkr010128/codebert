# coding: utf-8
# Your code here!
X,K,D=map(int,input().split())

move=min(abs(X)//D,K)
ans=abs(X)-move*D

if move==K:
    print(ans)
else:
    if (K-move)%2==0:
        print(ans)
    else:
        print(abs(ans-D))