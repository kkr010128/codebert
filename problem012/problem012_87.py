import math
def prime(n):
    if (n==2):
        return True
    if(n<2 or n%2==0):
        return False
    i=3
    while(i<=math.sqrt(n)):
        if (n%i==0):
            return False
        i=i+2
    return True

N=int(input())
count=0
for i in range(N):
    n=int(input())
    if(prime(n)):
        count+=1
print(count)