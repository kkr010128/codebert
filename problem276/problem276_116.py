N = int(input())
A = list(map(int, input().split()))

S = sum(A)
min_S = S
sum_B = 0
for i in range(N):
    sum_B += A[i]
    min_S = min(min_S, abs(sum_B - (S - sum_B)))

print(min_S)