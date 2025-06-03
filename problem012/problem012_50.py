import math
n=int(input())
s=0
for i in range(n):
    a=int(input())
    b=math.ceil(a**0.5)
    if a==2:
        s+=1
    elif a%2==0 or a < 2:
        continue
    else:
        c=0
        for j in range(3,b+1,2):
            if a%j==0:
                c+=1
                break
        if c==0:
            s+=1
print(s)