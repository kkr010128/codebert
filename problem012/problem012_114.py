import math
n=int(input())
s=0

for i in range(n):
    a=int(input())
    #b=int(a**0.5)
    b=math.ceil(a**0.5)
    #print(str(b), '??O') 
    if a==2:
        s+=1
   #     print(str(a),'!!!!')
    elif a%2==0 or a < 2:
        continue
    else:
        j=3
        c=0
        while j <= b:
            if a%j==0:
                c+=1
                break
            j+=2
        if c==0:
            s+=1
        """
        for j in range(3,b+1,2):
            if a%j==0:
                break
            if j==b:
                s+=1
                print(str(a),'!!!!')
"""
print(s)