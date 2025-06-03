import heapq

N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
L = []
ans = 0

heapq.heappush(L, -A[0])

for i in range(1, N):
    max = heapq.heappop(L)
    max *= -1
    ans += max
    heapq.heappush(L, -A[i])
    heapq.heappush(L, -A[i])

print(ans)

