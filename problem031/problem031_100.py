while True:
    result=0
    SS=0
    n=int(input())
    if n==0:
        break
    s=list(map(int,input().split()))
    average=(sum(s)/n)
    for i in s:
        SS=((average-i)**2)/n
        result+=SS
    print(result**(1/2))