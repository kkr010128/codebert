from collections import deque
N,M = map(int,input().split())
l = [[] for _ in range(N+1)]
 
for _ in range(M):
  a,b = map(int,input().split())
  l[a].append(b)
  l[b].append(a)

check = [0]*(N+1)
cnt = 0
for i in range(1,N+1):
  if check[i] == 1:
    continue
  st = deque([i])
  check[i] = 1
  while st:
    s = st.popleft()
    for t in l[s]:
      if check[t] == 0:
        check[t] = 1
        st.append(t)
      continue
  cnt += 1

print(cnt-1)