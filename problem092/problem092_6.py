# ABC172　C - Walking Takahashi
X,K,D=map(int,input().split())

q=abs(X)//D
if q>K:
    print(abs(X)-K*D)
else:
    if (K-q)%2==0:
        print(abs(X)-q*D)
    else:
        print(abs(abs(X)-(q+1)*D))