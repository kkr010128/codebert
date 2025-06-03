from collections import defaultdict
from collections import deque
from collections import Counter
import math

def readInt():
	return int(input())
def readInts():
	return list(map(int, input().split()))
def readChar():
	return input()
def readChars():
	return input().split()

n,k = readInts()
p = [0]+readInts()
c = [0]+readInts()

ans = -1*float("inf")
for i in range(1,n+1):
	j = p[i]
	t = [0]
	al = set()
	while j not in al:
		t.append(t[-1]+c[j])
		al.add(j)
		j = p[j]
	if t[-1]<=0:
		ans = max(ans, max(t[1:k+1]))
	else:
		kuri =(k-1)//(len(t)-1)
		s = kuri*t[-1]
		re = k -kuri*(len(t)-1)
		ans = max(ans, max(s,s+max(t[:re+1])))

print(ans)
