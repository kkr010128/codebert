import sys
import collections

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def main():
	#a = int(input())
	n , m = tin()
	#s = input()
	
	path = [[] for _ in range(n)]
	for _ in range(m):
		a, b = tin()
		path[a-1].append(b-1)
		path[b-1].append(a-1)
		
	nn = [-1]*n
	st=1
	for i, p in enumerate(nn):
		if nn[i] != -1:
			continue
		nn[i]=st
		cc = st
		st += 1
		q = collections.deque()
		q.append(i)
		while q:
			pos = q.popleft()
			for np in path[pos]:
				if nn[np] == -1:
					q.append(np)
					nn[np]=cc
	return cc-1
			
		
		
	
	
	
#+++++
isTest=False

def pa(*vl):
	if not isTest:
		return
	for v in vl:
		print(v)
		
def input_clipboard():
	import clipboard
	input_text=clipboard.get()
	input_l=input_text.splitlines()
	for l in input_l:
		yield l

if __name__ == "__main__":
	if sys.platform =='ios':
		if input_method==input_methods[0]:
			ic=input_clipboard()
			input = lambda : ic.__next__()
		elif input_method==input_methods[1]:
			sys.stdin=open('inputFile.txt')
		else:
			pass
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)