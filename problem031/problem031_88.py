import math
while True:
    n=int(input())
    if n==0:
        break
    s=list(map(int,input().split()))
    m=sum(s)/len(s)
    a=0
    for i in range(n):
        a+=(s[i]-m)**2
    b=math.sqrt(a/n)
    print('{:.5f}'.format(b))
