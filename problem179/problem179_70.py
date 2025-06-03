N,M=map(int,input().split())
A=list(map(int,input().split()))
B=[i for i in A if i >= sum(A)/(4*M)]
print("Yes" if len(B)>=M else "No")