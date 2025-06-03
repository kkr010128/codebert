N,K=list(map(int,input().split()))
A = [int(x) for x in input().split()]
A.sort()
print(sum(A[:K]))