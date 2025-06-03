N, M = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)
base = total  / (4 * M)

filtered = list(filter(lambda x: x >= base, A))

if (len(filtered) >= M):
    print('Yes')
else:
    print('No')

