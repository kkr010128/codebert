import itertools
while True:
    n,x=map(int,input().split())
    if n==0 and x==0:
        break
    z=list(range(1,n+1))
    a=list(itertools.combinations(z,3))
    b=[]
    for i in a:
        b+=[sum(i)]
    print(b.count(x))