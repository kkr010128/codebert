n, m = map(int, input().split())
route = [[] for _ in range(n+1)]
ans = [0]*n

for _ in range(m):
    a, b = map(int, input().split())
    route[a].append(b)
    route[b].append(a)

q = [1]
l = set()

while True:
    if len(q) == 0:
        break
    p = q.pop(0)
    for i in route[p]:
        if i not in l:
            l.add(i)
            ans[i-1] = p
            q.append(i)

if ans.count(0) > 1:
    print("No")
else:
    print("Yes")
    for i in range(1, n):
        print(ans[i])