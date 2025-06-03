N = int(input())
A = list(map(int, input().split()))

ans = [0, 0]
ans_abs = 10**200

A_sum = sum(A)
A_1 = 0
A_2 = A_sum

for i in range(N - 1):
    A_1 += A[i]
    A_2 -= A[i]
    ans_abs = min(ans_abs, abs(A_1 - A_2))

print(ans_abs)