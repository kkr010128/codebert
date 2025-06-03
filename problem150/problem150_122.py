N, K = map(int, input().split())
A = list(map(lambda x: int(x)-1, input().split()))
now = 0
route = [now]
visited = set()
visited.add(now)
while A[now] not in visited:
    route.append(A[now])
    visited.add(A[now])
    now = A[now]
L = len(route)
looplen = L-route.index(A[now])
if K < L:
    print(route[K]+1)
else:
    print(route[L-looplen+(K-L)%looplen]+1)