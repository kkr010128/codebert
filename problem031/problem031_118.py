import math
while True:
    n=int(input())
    if n==0:
        break
    s=list(map(int,input().split()))
    m=sum(s)/n
    aa=0
    for i in s:
        aa+= (i-m)**2
    a=math.sqrt((aa)/n)
    print(f'{a:.08f}')
