import math

X,K,D = map(int,input().split())
X = abs(X)

if X > K*D:
    print(X-K*D)
else:
    c=math.floor(X/D)
    print( abs(X-D*c-((K-c)%2)*D) )
 