import itertools
import functools
import math

def OK():
    N = int(input())

    sum = 0
    cnt = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            chk = math.gcd(i,j)
            for k in range(1,N+1):
                sum += math.gcd(chk,k)

    print(sum)

OK()
