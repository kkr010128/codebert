X,N=map(int,input().split())
P=[int(x) for x in input().split()]
index=0
while(1):
    if X-index not in P:
        print(X-index)
        break
    if X+index not in P:
        print(X+index)
        break
    index+=1