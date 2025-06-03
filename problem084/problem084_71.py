from collections import defaultdict, deque
dic = defaultdict(list)
N, M  = map(int, input().split())
for i in range(M):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)
ans = 0
now = 1
seen = [-1]*N
queue = deque()

for i in range(N):
    if seen[i]!=-1:
        continue
    queue.append(i+1)
    seen[i]=now
    temp=0
    while queue:
        temp+=1
        q = queue.popleft()
        for j in dic[q]:
            if seen[j-1]!=-1:
                continue
            queue.append(j)
            seen[j-1]=now
    now+=1
    ans = max(ans, temp)

print(ans)