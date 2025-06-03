import heapq

def solve():
    N = int(input())
    A = list(sorted(map(int, input().split()), reverse=True))
    C = [-A[0]]

    ans = 0
    for a in A[1:]:
        K = heapq.heappop(C)
        ans += -K
        heapq.heappush(C, -a)
        heapq.heappush(C, -a)

    print(ans)



solve()