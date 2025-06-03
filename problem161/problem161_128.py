def f(A,B,x):
	val=((A*x)//B)-A*(x//B)
	return val

A,B,n=map(int,input().split())
print(f(A,B,B-1)) if n>=B-1 else print(f(A,B,n))