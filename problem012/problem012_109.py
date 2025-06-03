import math

n = int(raw_input())

def isPrime(a):
    if a==2 or a==3:
        return 1
    if a<2 or a%2==0:
        return 0
        
    i = int(math.sqrt(a))+1
    for x in xrange(3,i):
        if a%x==0:
            return 0
    return 1

cnt = 0
for _ in xrange(n):
    a = int(raw_input())
    cnt += isPrime(a)
print cnt