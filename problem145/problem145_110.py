from collections import deque

mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

N,M = MI()
links = [[] for _ in range(N)]

for _ in range(M):
    a, b = MI()
    a -= 1
    b -= 1
    links[a].append(b)
    links[b].append(a)

ans = [-1] * N
ans[0] = 0
q = deque([(0, 0)])
while q:
  room, prev = q.popleft()
  for next_ in links[room]:
    if ans[next_] < 0:
      ans[next_] = room+1
      q.append((next_, room))
print("Yes")
for i in range(1,N):
  print(ans[i])             