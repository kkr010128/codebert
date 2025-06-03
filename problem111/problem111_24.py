import heapq
n = int(input())
A = list(map(int, input().split()))
A = sorted(A, reverse=True)
ans = 0
q = []
heapq.heappush(q, A[0]*-1)
for i in range(1, n):
    tmp = heapq.heappop(q)
    ans += tmp
    heapq.heappush(q, A[i] * -1)
    heapq.heappush(q, A[i] * -1)

print(ans*-1)