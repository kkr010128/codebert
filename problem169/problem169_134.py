N=int(input())
A=list(map(int,input().split()))
B=list(range(1, N + 1))
import collections
new_A=collections.Counter(A)
for i in B:
    print(new_A[i])
