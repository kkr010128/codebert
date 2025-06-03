import math
while True:
    n,x=list(map(int,input().split()))
    if n==x==0: break
    c=0
    for i in range(1,x//3):
        if i>n: break
        for j in range(i+1,(x-i)//2+1):
            if j>n: break
            k=x-i-j
            if not (n<k or k<=j):
                c+=1
    print(c)