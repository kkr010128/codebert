N,K=input().split()
N=int(N)
K=int(K)
a=[]
a=[int(a) for a in input().split()]
a.sort()
print(sum(a[0:K]))