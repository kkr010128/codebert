from collections import deque
N = int(input())
A = deque(list(map(int, input().split())))

ans = 0
cnt = 1
while A:
    a = A.popleft()
    if cnt == a:
        cnt += 1
        continue
    else:
        ans += 1
if ans == N:
    print(-1)
else:
    print(ans)