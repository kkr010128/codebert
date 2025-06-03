import math
import collections
import copy
import sys

n = int(input())

a = list(map(int,input().split()))

limit = 10 ** 6

sCheck = math.gcd(a[0],a[1])
if n == 2:
    if sCheck == 1:
        print("pairwise coprime")
    else:
        print("not coprime")
    sys.exit()
else:
    for i in range(2,n):
        sCheck = math.gcd(sCheck,a[i])


beforeQ = collections.deque([int(i) for i in range(3,(limit + 1))])
D = dict()
p = 2
D[2] = 2
D[1] = 1

while p < math.sqrt(limit):
    afterQ = collections.deque()
    while len(beforeQ) > 0:        
        k = beforeQ.popleft()
        if k % p != 0:
            afterQ.append(k)
        else:
            D[k] = p
    beforeQ = copy.copy(afterQ)
    p = beforeQ.popleft()
    D[p] = p
while len(beforeQ) > 0:
    k = beforeQ.popleft()
    D[k] = k
    
ansSet = set()
count = 0

for i in a:
    k = i
    kSet = set()
    while k != 1:
        if D[k] in ansSet:
            if not(D[k] in kSet):
                count = 1
                break
        else:
            ansSet.add(D[k])
            kSet.add(D[k])
        k = int(k // D[k])
    if count == 1:
        break

if count == 0:
    print("pairwise coprime")
elif sCheck == 1:
    print("setwise coprime")
else:
    print("not coprime")