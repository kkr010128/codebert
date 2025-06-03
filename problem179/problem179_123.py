N, M = map(int, input().split())
A = list(map(int, input().split()))

m = 0
for a in A:
    if a >= sum(A) / (4 * M):
        m += 1

print('Yes') if m >= M else print('No')