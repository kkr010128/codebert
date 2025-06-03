import math
while True:
    n=int(input())
    if n==0:
        break
    else:
        a=list(map(int,input().split()))
        m=sum(a)/n
        l=0
        for i in range(n):
            l+=(a[i]-m)**2
        b=math.sqrt(l/n)
        print("{:.8f}".format(b))
