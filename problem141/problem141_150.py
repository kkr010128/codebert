N = int(input())

A = [int(i) for i in input().split()]

if N == 0 and A[0] != 1:
    print(-1)
    exit()

nodes = [0] * (N+1)
nodes[0] = 1
for i in range(1, N+1):
    node = (nodes[i-1]-A[i-1])*2
    if node < A[i]:
        print(-1)
        exit()
    nodes[i] = node

#print(nodes)

nodes[-1] = A[-1]
for i in range(N-1, -1, -1):
    nodes[i] = min(nodes[i], nodes[i+1]+A[i])

#print(nodes)

print(sum(nodes))