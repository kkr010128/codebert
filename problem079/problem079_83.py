from math import factorial

def comb(a,b):
    return factorial(a)//(factorial(b)*factorial(a-b))

n = int(input())
ans=0
for i in range(1,n//3+1):
    ans+=comb(n-3*i+(i-1),i-1)
print(ans%(10**9+7))
