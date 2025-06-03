N = int(input())
A = list(map(int, input().split()))

d = [1] * (N+1)
d[0] -= A[0]
for i in range(N):
    d[i+1] = d[i] * 2 - A[i+1]
if d[-1] < 0:
    print(-1)
    exit()

d[-1] = A[-1]
for i in range(N, 0, -1):
    d[i-1] = min(d[i]+A[i-1], d[i-1]+A[i-1])
print(sum(d))
