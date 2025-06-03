#python2.7

N=input()
A=map(int,raw_input().split())
num=0

for i in range(N):
	minj=i
	for j in range(N-i):
		if A[j+i] < A[minj]:
			minj=j+i
	if i != minj:
		A[i],A[minj]=A[minj],A[i]
		num+=1

for m in range(N-1):
	print str(A[m]),

print A[N-1]
print num