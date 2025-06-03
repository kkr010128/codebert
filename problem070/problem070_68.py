import queue

N, M = map(int, input().split())
e = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    e[A].append(B)
    e[B].append(A)
# print(e)

seen = [-1] * N
k = -1
for i in range(N):
    if seen[i] == -1:
        k += 1
        seen[i] = k
        que = queue.Queue()
        que.put(i)
        while not que.empty():
            v = que.get()
            for nv in e[v]:
                if seen[nv] != -1: continue
                seen[nv] = k
                que.put(nv)
# print(seen)
print(k)
