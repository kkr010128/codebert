
from sys import stdin

input = stdin.readline().rstrip

#x = input().rstrip()
#n = int(input())

#a,b,c = input().split()
#a,b,c = map(int, input().split())

D,T,S = map(int, input().split(" "))

if(T * S >= D):
	print("Yes")
else:
	print("No")
