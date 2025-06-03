while 1:
    r=0
    S=0
    n=int(input())
    if n==0:break
    s=list(map(int,input().split()))
    a=(sum(s)/n)
    for i in s:
        S=((a-i)**2)/n
        r+=S
    print(r**0.5)