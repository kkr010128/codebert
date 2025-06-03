N, K = map(int, input().split()) 

P=list(map(int,input().split()))

list.sort(P)

from itertools import accumulate
ans = list(accumulate(P))

print(ans[K-1])