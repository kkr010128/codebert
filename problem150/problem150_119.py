N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))

visited = [0] * (N + 1)
route = [0] * (N + 1)
next_ = 1
count = 0

for i in range(K + 1):
    if visited[next_] != 0:
        x = visited[next_]
        count = (K - (x - 1)) % (i + 1 - x) + x
        print(route[count])
        exit()
    visited[next_] = i + 1
    route[i + 1] = next_
    next_ = A[next_]

print(route[K + 1])
