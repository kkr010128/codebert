import queue

ans = 0

N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
q = queue.Queue()
q.put(0)
for a in range(len(A)):
    ans += q.get()
    q.put(A[a])
    if a != 0:
        q.put(A[a])

print(ans)
