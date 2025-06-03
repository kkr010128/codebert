N = int(input())
A = list(map(int, input().split()))

s = sum(A)
r = 10**10
n = 0
for i in range(N-1):
    n += A[i]
    r = min(abs(s-n*2), r)

print(r)