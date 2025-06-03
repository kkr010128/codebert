import math
while True:
    n=int(input())
    if n==0:
        break
    else:
        s=list(map(int,input().split()))
        S=sum(s)
        m=S/n
        a2=0
        for j in range(n):
            a2+=(s[j]-m)**2
        a2=a2/n
        a=math.sqrt(a2)
        print(f'{a:.4f}')
