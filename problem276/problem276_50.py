from collections import defaultdict

def readInt():
	return int(input())
def readInts():
	return list(map(int, input().split()))
def readChar():
	return input()
def readChars():
	return input().split()

n = readInt()
a = readInts()
sum_a = sum(a)
v = sum(a)/2
ans = float("inf")
t = 0
for i in range(len(a)):
	t+=a[i]
	ans = min(ans,abs(sum_a-2*t))
print(ans)