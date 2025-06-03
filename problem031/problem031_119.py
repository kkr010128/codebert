import math
while True:
    n=int(input())
    if n==0:
        break
    s=list(map(int,input().split()))
    m=sum(s)/n
    S=0
    for i in range(n):
        S+=(s[i]-m)**2
    a2=math.sqrt(S/n)
    
    print('{:.8f}'.format(a2))
