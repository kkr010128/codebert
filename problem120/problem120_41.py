N,K=input().split()
N=int(N)
K=int(K)

p = [int(i) for i in input().split()]
p.sort()
print(sum(p[0:K]))
