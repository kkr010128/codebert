N,K = map(int,input().split())

min = N%K
if min>abs(min-K):
  min = abs(min-K)

print (min)