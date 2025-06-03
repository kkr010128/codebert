from collections import defaultdict

def readInt():
	return int(input())
def readInts():
	return list(map(int, input().split()))
def readChar():
	return input()
def readChars():
	return input().split()

x = readInt()

for i in range(int(x//105),int(x//100)+2):
	t = x-100*i
	if 0<=t and t<=5*i:
		print(1)
		exit()
print(0)