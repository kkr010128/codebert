N = int(input())
A = list(map(int, input().split()))
total = 1000
for i in range(1, N):
    if A[i] > A[i-1]:
        total += (total // A[i-1]) * (A[i]-A[i-1])
print(total)
