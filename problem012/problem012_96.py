from math import sqrt
def isprime(inlst, i, sq):
    while sq >= i:
    	inlst = [x for x in inlst if x%i > 0 or x == i]
    	i += 2
    return inlst
n = int(input())
inlst = []
for i in range(n):
    inlst.append(int(input()))
inlst = [x for x in inlst if x%2 > 0 or x == 2]
i = 3
maxin = max(inlst)
inlst = isprime(inlst, i, int(sqrt(maxin)) + 1)
print(len(inlst))