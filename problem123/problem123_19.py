import functools
N = int(input())

A = list(map(int,input().split()))
#print(A)
s = A[0]
for num in A[1:]:
    s ^= num

res = [0] * N
for i,num in enumerate(A):
    res[i] = s^num
print(*res)