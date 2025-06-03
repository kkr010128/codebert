import sys
from collections import defaultdict

#+++++
		
def main():
	n, k = map(int, input().split())
	aal = list(map(int, input().split()))
	
	sss = [0]*(n+1)
	si=0
	for i, a in enumerate(aal):
		si+=a-1
		sss[i+1]=si%k
	
	count=0
	mkl_dict=defaultdict(lambda :0)
	for j in range(n+1):
		sj=sss[j]
		if j-k >= 0:
			mkl_dict[sss[j-k]]-=1
		count += mkl_dict[sj]
		mkl_dict[sj] += 1
			
	print(count)
	
	
#+++++
isTest=False

def pa(v):
	if isTest:
		print(v)

if __name__ == "__main__":
	if sys.platform =='ios':
		sys.stdin=open('inputFile.txt')
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)