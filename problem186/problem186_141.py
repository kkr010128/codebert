K, N = [int(x) for x in input().split()]
A = list([int(x) for x in input().split()])

result = []

for i in range(N):
    if i == N - 1:
        result.append(K - A[i] + A[0])
    else:
        result.append(A[i + 1] - A[i])

result.sort()

print(sum(result[:-1]))
