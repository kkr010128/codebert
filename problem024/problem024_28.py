import sys
input = lambda: sys.stdin.readline()[:-1]
n,k=map(int,input().split())
w = [int(input()) for i in range(n)][::-1]
def maxnumber(p): 
	wc=w.copy()
	for i in range(k):
		lim=p
		while len(wc):
			if wc[-1]<=lim:
				lim-=wc.pop()
			else:break
	return len(wc)

minp=float('inf')
left,right=1,10**9+1
while left<right:
	mid=(left+right)//2
	maxn=maxnumber(mid)
	if maxn>0:
		left=mid+1
	else:
		right=mid
		minp=min(mid,minp)
print(minp)






	

