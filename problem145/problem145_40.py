from collections import deque

n,m,*ab = map(int, open(0).read().split())

to = [[] for _ in range(n+1)]
for i in range(0, m*2, 2):
    a = ab[i]
    b = ab[i+1]
    to[a].append(b)
    to[b].append(a)

ans = [None]*(n+1)
q = deque([1])
while q:
    p = q.pop()
    children = to[p]
    for child in children:
        if ans[child] is None:
            ans[child] = p
            q.appendleft(child)

print("Yes")
print("\n".join(map(str, ans[2:])))