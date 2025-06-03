A,B,N=map(int,input().split())
max_L=0
x=0
if B>N:
	x=N
	max_L=int(A*x/B)-A*int(x/B)
else:
	x=B-1
	max_L=int(A*x/B)-A*int(x/B)

print(max_L)