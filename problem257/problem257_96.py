N = int(input())
A = tuple(map(int, input().split()))
x = [[] for _ in range(N + 1)]
for i, a in enumerate(A):
    x[a].append(i)

maxcount = 0
todo = [(1, i) for i in x[1]]
while todo:
    a, i = todo.pop()
    maxcount = max(maxcount, a)
    if a == N:
        continue
    na = a + 1
    for ni in x[na]:
        if ni < i:
            continue
        todo.append((na, ni))
if maxcount > 0:
    print(N - maxcount)
else:
    print(-1)