from collections import deque
n = int(input())
l = list(map(int,input().split()))
l.sort()
largest = l[-1]
que = deque(l)
cnt = n
ans = 0
while cnt > 0:
    x = que.pop()
    ans += x
    cnt -= 1
    if cnt != 0:
        ans += x
        cnt -= 1
print(ans-largest)