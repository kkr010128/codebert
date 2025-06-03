import itertools, math
from functools import reduce
def gcd(*numbers):
    return reduce(math.gcd, numbers)
    
K = int(input())
if K == 1:
    print(1)
    exit()
elif K ==2:
    print(9)
    exit()
l_2 = itertools.combinations(range(1, K + 1), 2)
l_3 = itertools.combinations(range(1, K + 1), 3)
sum = int(K * (K + 1) / 2)
for x in l_2:
    sum += math.gcd(x[0], x[1]) * 6
for x in l_3:
    sum += gcd(x[0], x[1], x[2]) * 6
print(sum)