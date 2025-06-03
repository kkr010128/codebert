import math
while True:
    n=int(input())
    if n==0:break
    else:
        s = list(map(int, input().split())) #入力の値が横並びの時使う
        x=sum(s)
        y=x/n
        a=0
        for i in range(n):
             z=(s[i]-y)**2
             a+=z
        b=math.sqrt(a/n)
        print(format(b, '.8f'))
