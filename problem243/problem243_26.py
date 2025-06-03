import sys
#input = sys.stdin.buffer.readline

# mod=10**9+7
# rstrip().decode('utf-8')
# map(int,input().split())
# import numpy as np


def main():
	n=int(input())
	s=[]
	t=[]
	for i in range(n):
		a,b=input().split()
		s.append(a)
		t.append(int(b))
	x=input()
	for i in range(n):
		if x==s[i]:
			print(sum(t[i+1:]))


if __name__ == "__main__":
	main()
