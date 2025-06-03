from collections import deque
N = int(input())
A = sorted(map(int, input().split()), reverse=True)

ans = A[0]
q = deque((A[1], A[1]))
for i in range(2, N):
    ans += q.popleft()
    q.append(A[i])
    q.append(A[i])
print(ans)