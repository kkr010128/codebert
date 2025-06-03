N = int(input())
A = list(map(int, input().split()))

numbers = []

s = A[0]
for i in range(1, N):
    s = s ^ A[i]
for i in range(N):
    numbers.append(s ^ A[i])

print(*numbers)
