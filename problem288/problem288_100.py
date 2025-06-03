import math
N=int(input())
a=1
sum=N
flag=True
while flag:
    if a>math.sqrt(N):
        break
    if N%a==0:
        b=N//a
        if sum>a+b-2:
            sum=a+b-2
    a+=1
print(sum)