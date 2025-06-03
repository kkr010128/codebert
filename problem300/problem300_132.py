import math

def enum_div(n):
    ir=int(n**(0.5))+1
    ret=[]
    for i in range(1,ir):
        if n%i == 0:
            ret.append(i)
            if (i!= 1) & (i*i != n):
                ret.append(n//i)
    return ret

def isPrime(x):
    if x < 2:
        return 0
    elif x == 2:
        return 1
    if x%2 == 0:
        return 0
    ir=int(x**(0.5))+1
    for i  in range(3,ir,2) :
        if x%i == 0:
            return 0
    return 1

a,b=map(int,input().split())
c=math.gcd(a,b)

if isPrime(c)==1:
    print(2)
else:
    icnt=0
    for i in enum_div(c):
        if isPrime(i)==1:
            icnt+=1
    print(icnt+1)