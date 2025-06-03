import sys
N = int(input())
A = list(map(int, input().split()))
cusum = [0 for i in range(N+1)]
cusum[N] = A[N]

if N == 0 and A[0] > 1:
    print(-1)
    sys.exit()

for i in range(N-1, -1, -1):
    cusum[i] = cusum[i+1] + A[i]

# print(cusum)
pre_node = 1
ans = 1
for i in range(1, N+1):
    node = (pre_node - A[i-1]) * 2
    if node < A[i]:
        ans = -1
        break
    pre_node = min(node, cusum[i])
    ans += pre_node
print(ans)
    
