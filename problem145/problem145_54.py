N, M = map(int, input().split())
route = [[] for _ in range(N)]
sign = [0]*N

#print(route)
for i in range(M):
    a,b = map(int, input().split())
    route[a-1].append(b-1)
    route[b-1].append(a-1)
#print(route)

marked = {0}
q = [0]
for i in q:
    for j in route[i]:
        if j in marked:
            continue
        q.append(j)
        marked.add(j)
        sign[j] = i+1

print('Yes')
[print(i) for i in sign[1:]]