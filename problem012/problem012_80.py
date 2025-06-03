from math import sqrt
def isprime(inlst, chk, sq):
	for i in range(3, sq, 2):
		inlst = [x for x in inlst if x%i > 0 or x == i]
		i += 2
	return inlst
n = int(input())
inlst = [input() for i in range(n)]
inlst = [int(i) for i in inlst]
inlst = [x for x in inlst if x%2 > 0 or x == 2]
inlst = isprime(inlst, 3, int(sqrt(max(inlst))) + 1)
print(len(inlst))