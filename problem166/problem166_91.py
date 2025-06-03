import collections
from math import factorial

def permutations_count(n, r):
    ''' 順列 '''
    return factorial(n) // factorial(n - r)

def combinations_count(n, r):
    ''' 組み合わせ '''
    return factorial(n) // (factorial(n - r) * factorial(r))


S = input()

lis = []
amari = 1
lis.append(int(S[-1]))

for i in range(2,len(S)+1):
    amari = (amari * 10) % 2019
    lis.append((int(S[-1*i]) * amari + lis[i-2]) % 2019)

c = collections.Counter(lis)

su = 0

for k in c:
    if c[k] > 1:
        su += combinations_count(c[k], 2)
        
        
        
su += c[0]

print(su)