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

k = readInt()

n = 7
for i in range(10**6):
	if n%k==0:
		print(i+1)
		exit()
	else:
		n = (n*10+7)%k

print(-1)