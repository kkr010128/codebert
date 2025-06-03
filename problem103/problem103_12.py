N = int(input())
A = list(map(int, input().split()))

B = []
temp = 0
for i in range(N):
    if A[i] != temp:
        B.append(A[i])
        temp = A[i]

N = len(B)
A = [float("inf")] + B + [0]

money, stock = 1000, 0
for i in range(1, N + 1):
    if A[i - 1] > A[i] and A[i] < A[i + 1]:
        x = money // A[i]
        money -= A[i] * x; stock += x
    if A[i - 1] < A[i] and A[i] > A[i + 1]:
        x = stock
        money += A[i] * x; stock -= x

print(money)
