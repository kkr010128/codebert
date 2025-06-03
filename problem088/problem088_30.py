N = int(input())
A = list(map(int,input().split()))
a = 0
for i in range(1, N):
    b = A[i]-A[i-1]
    if b < 0:
        A[i] = A[i-1]
        a -= b
print(a)