# C - Replacing Integer

n,k = map(int,input().split())

m = n % k
l = map(abs,[m-k,m,m+k])
print(min(l))
