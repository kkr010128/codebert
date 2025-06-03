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

s = list(input())
k = readInt()

if len(Counter(s))==1:
	ans = k*len(s)//2
elif s[0]!=s[-1]:
	ans = 0
	i = 0
	l = 0
	tmp = s[:]+["!"]
	d = []
	while i<len(s):
		if tmp[i]==tmp[i+1]:
			i+=1
		else:
			d.append(tmp[l:i+1])
			l = i+1
			i+=1
	for i in d:
		ans+=len(i)//2
	ans*=k
else:
	ans = 0
	i = 0
	l = 0
	tmp = s[:]+["!"]
	d = []
	while i<len(s):
		if tmp[i]==tmp[i+1]:
			i+=1
		else:
			d.append(tmp[l:i+1])
			l = i+1
			i+=1
	for i in d[1:-1]:
		ans+=len(i)//2
	ans*=k
	ans+=len(d[0])//2
	ans+=len(d[-1])//2
	ans+=(len(d[0])+len(d[-1]))//2*(k-1)


print(ans)