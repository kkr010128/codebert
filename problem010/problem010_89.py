N=input()
A=map(int,raw_input().split())
for i in range(N-1):
	for k in range(N-1):
		print A[k],
	print A[N-1]
	v=A[i+1]
	j=i
	while j>=0 and A[j] >v:
		A[j+1]=A[j]
		j=j-1
	A[j+1]=v

for m in range(N-1):
	print str(A[m]),
print A[N-1]