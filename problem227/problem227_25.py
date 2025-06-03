N,K = map(int,input().split())

a = sorted(list(map(int,input().split())),reverse=True)
del a[0:K]
print(sum(a))