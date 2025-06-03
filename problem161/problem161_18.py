A,B,N=map(int,input().split())
f=lambda x:(A*x)//B-A*(x//B)
print(f(B-1 if B-1<=N else N))