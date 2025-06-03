while True:
    n=int(input())
    if n==0:break
    s=list(map(float,input().split()))
    print((sum(map(lambda x: x*x,s))/n-(sum(s)/n)**2)**.5)
