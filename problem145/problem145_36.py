N, M = map(int,input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
prev = [0] * N
to_list = [ [] for _ in range(N)]
for a,b in AB:
 to_list[a - 1].append(b - 1)
 to_list[b - 1].append(a - 1)
marked = {0}
que = [0]
for i in que:
   for j in to_list[i]:
       if j in marked: continue
       que.append(j)
       marked.add(j)
       prev[j] = i+1
print('Yes')
print(*prev[1:], sep='\n')