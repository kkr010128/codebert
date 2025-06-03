from math import sqrt
N = input()
sum = 0
for _ in xrange(N):
    n = input()
    for i in xrange(2,int(sqrt(n))+1):
        if n%i == 0:
            break
    else:
        sum += 1
print sum