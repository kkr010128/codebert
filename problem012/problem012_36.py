import math
def isprime(n):
    if n==1:
        return False
    elif n==2:
        return True
    k=int(math.sqrt(n))+1
    for i in range(2,k+1):
        if n%i==0:
            return False
    return True
N=int(input())
ans=0
for i in range(N):
    if isprime(int(input())):
        ans+=1
print(ans)

