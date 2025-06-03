X,N=map(int,input().split())
p=list(map(int,input().split()))
upper=float("inf")
lower=float("inf")
a=X
b=X
while True:
    if not a in p:
        upper=a
        break
    a+=1
while True:
    if not b in p:
        lower=b
        break
    b-=1
if abs(upper-X)==abs(lower-X):
    print(lower)
elif abs(upper-X)>abs(lower-X):
    print(lower)
else:
    print(upper)