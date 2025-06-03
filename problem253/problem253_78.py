N,A,B=map(int,input().split())
if (A+B)%2==0:
	P=(B-A)//2
else:
	P=float("inf")
if (A+B)%2==1:
	Q=A
	Q+=(B-Q-(B-Q+1)//2)
else:
	Q=float("inf")

if (A+B)%2==1:
	R=N-B+1
	B=N
	A+=R
	R+=B-(A+B)//2
else:
	R=float("inf")
print(min(P,Q,R))