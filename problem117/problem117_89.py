import itertools
import bisect
n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
sum_a=list(itertools.accumulate(a))
sum_b=list(itertools.accumulate(b))
result=bisect.bisect_right(sum_b,k)

for i in range(n):
    if sum_a[i]<=k:
        result=max(result,i+1+bisect.bisect_right(sum_b,k-sum_a[i]))
print(result)