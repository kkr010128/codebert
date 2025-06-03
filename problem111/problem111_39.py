from collections import deque
n = int(input())
A = sorted(list(map(int, input().split())))[::-1]

deq = deque([A[0]])
ans = 0
for x in A[1:]:
    ans += deq.popleft()
    deq.append(x)
    deq.append(x)
print(ans)