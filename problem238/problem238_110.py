n,k,s=map(int,input().split())
sMax=10**9
if k==0:
    if s==sMax:
        print("1 "*n)
    else:
        print((str(sMax)+" ")*n)
else:
    if s==sMax:
        print((str(s)+" ")*k+"1 "*(n-k))
    else:
        print((str(s)+" ")*k+(str(sMax)+" ")*(n-k))