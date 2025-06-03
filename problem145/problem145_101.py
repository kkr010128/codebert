from collections import deque

n, m = map(int,input().split())
ex = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    ex[a].append(b)
    ex[b].append(a)

d = deque()
d.append(1)
ans = [-1] * (n+1)
ans[1] = 1
while d:
    f = d.popleft()
    for t in ex[f]:
        if ans[t] == -1:
            ans[t] = f
            d.append(t)

for i in range(2, n+1):
    if ans[i] == -1:
        print('No')
        exit()

print('Yes')
for i in range(2,n+1):
    print(ans[i])