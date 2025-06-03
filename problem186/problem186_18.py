K,N=map(int,input().split())
A=[int(x) for x in input().split()]
A+=[K+A[0]]
print(K-max(A[i+1]-A[i] for i in range(N)))
