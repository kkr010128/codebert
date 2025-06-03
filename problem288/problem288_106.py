import numpy
n = int(input())
l = []
ans = n

def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1

if is_prime(n) :
    print(n-1)
if is_prime(n) == False:
    for i in range(2,int(numpy.sqrt(n))+1):
        if n%i == 0:
            a = i
            b = n//i
            ans = min(n,a+b-2)
    print(ans)