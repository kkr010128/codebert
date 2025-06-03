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

v = sum(a)/2
t = 0
for i in range(len(a)):
	t+=a[i]
	if t>v:
		break
z1 = sum(a[:i])
k1 = sum(a[i:])
z2 = sum(a[:i+1])
k2 = sum(a[i+1:])
if abs(z1-k1)<abs(z2-k2):
	z = z1
	k = k1
else:
	z = z2
	k = k2

print(abs(z-k))
