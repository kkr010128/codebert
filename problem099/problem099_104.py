from math import *

def trycut(val):
	ret = 0
	for i in range(n):
		ret += ceil(a[i]/val)-1
	return ret 

n,k=map(int,input().split())
a = [int(i) for i in input().split()]

low = 0
high = 1000000000
ans  =-1

while low <= high:
	mid = (low + high)/2
	cut = trycut(mid)
	# ~ print("low=",low, "high=", high,"val = ",mid,"ret = ",cut)
	if cut <= k:
		high = mid-0.0000001
		ans = mid
	else:
		low =  mid+0.0000001
	# ~ if low < high: print(low, high, "je reviens")
ans = int(ans*1000000)/1000000
# ~ print(ans)
print(int(ceil(ans)))


