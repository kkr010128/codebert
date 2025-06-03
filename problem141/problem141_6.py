N = int(input())
A = list(map(int, input().split()))

node = [[] for i in range(N + 1)]
idx = list(range(N+1))  # 0 ~ N
idx = idx[1:]  # 1 ~ N

# Depth = N
node[0].append(A[N])
node[0].append(A[N])

for i in idx:
    # min
    node[i].append(- (- node[i - 1][0] // 2) + A[- i - 1])
    # max
    node[i].append(node[i - 1][1] + A[- i - 1])

if 1 not in node[-1]:
    print(-1)
    exit()

node.reverse()
idx = list(range(N + 1))
idx = idx[1:]
maximum = []
maximum.append(1)

for i in idx:
    val = min(node[i][1], (maximum[i - 1] - A[i - 1]) * 2)
    maximum.append(val)

print(sum(maximum))
