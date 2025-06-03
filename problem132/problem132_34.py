N, K = map(int, input().split())
*A, = map(int, input().split())

b = [i for i in A]
for c in range(K):
    buf = [0]*(N+1)
    for i, j in enumerate(b):
        buf[max(i-j, 0)] += 1
        buf[min(i+j+1, N)] -= 1
    for i in range(1, N+1):
        buf[i] += buf[i-1]
    b = [buf[i] for i in range(N)]
    if all([i==N for i in b]):
        break

print(*b)