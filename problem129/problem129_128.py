from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

DP = [0] * (10 ** 6 + 1)

A.sort()
Sum = 0

d = defaultdict(int)
for key in A:
    d[key] += 1

for i in range(N):

    if DP[A[i]] == 0:
        for j in range(1, 10 ** 6):
            if A[i] * j <= 10 ** 6:
                DP[A[i] * j] = 1
            else:
                break

        if d[A[i]] == 1:
            Sum += 1
print(Sum)
