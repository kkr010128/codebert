from math import factorial
N = int(input())
A = list(map(int, input().split()))
n = {}
s = 0
for i in range(N):
    if A[i] not in n:
        n[A[i]] = 1
    else:
        n[A[i]] += 1
for j in n:
    if n[j] > 1:
        s += factorial(n[j]) // 2 // factorial(n[j]-2)
for i in range(N):
    print(s-n[A[i]]+1)
