from collections import deque

N,M = (int(a) for a in input().split())
g = [[] for _ in range(N)]
s = [0]*N
for i in range(M) :
    A,B = (int(a) for a in input().split())
    g[A-1].append(B)
    g[B-1].append(A)
visited = {0}
stack = [0]
for i in stack :
    for j in g[i] :
        if j-1 in visited :
            continue
        stack.append(j-1)
        visited.add(j-1)
        s[j-1] = i + 1
if s.count(0) > 1 :
    print("No")
else :
    print("Yes")
    print(*s[1:])







