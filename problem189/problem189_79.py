N, M = map(int, input().split(' '))
result = 0
if N > 1:
    result += N * (N - 1) / 2
if M > 1:
    result += M * (M - 1) / 2
print(int(result))