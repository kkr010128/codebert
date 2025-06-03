import collections
N=int(input())
A=[x for x in input().split()]
c = collections.Counter(A)
for i in range(N):
	print(c["{}".format(str(i+1))])