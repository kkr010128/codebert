from collections import defaultdict

def readInt():
	return int(input())
def readInts():
	return list(map(int, input().split()))
def readChar():
	return input()
def readChars():
	return input().split()

n,a,b = readInts()

if (b-a)%2==0:
	print((b-a)//2)
else:
	print(min(b-1,n-a,a+(b-a-1)//2,n-(a+b-1)//2))