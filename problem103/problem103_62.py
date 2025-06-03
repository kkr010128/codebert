import sys
from collections import deque,defaultdict

I=sys.stdin.readline

def ii():
	return int(I().strip())
def li():
	return list(map(int,I().strip().split()))

def mi():
	return map(int,I().strip().split())


def main():
	n=ii()
	arr=li()
	p=1000
	for i in range(n-1):
		if arr[i]==arr[i+1]:
			pass
		elif arr[i]<arr[i+1]:
			buy=p//arr[i]
			p+=(arr[i+1]-arr[i])*buy

	
	print(p)








		


		










		






if __name__ == '__main__':
	main()