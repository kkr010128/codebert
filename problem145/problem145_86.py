from collections import deque
from sys import stdin
input = stdin.readline


def main():
  N, M = list(map(int, input().split()))
  G = [[] for _ in range(N+1)]
  for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

  from_ = [0]*(N+1)

  q = deque([1])
  seen = set()
  seen.add(1)

  while len(q):
    now = q.popleft()
    for next_ in G[now]:
      if next_ not in seen:
        seen.add(next_)
        q.append(next_)
        from_[next_] = now

  print('Yes')
  for i in range(2, N+1):
    print(from_[i])


if(__name__ == '__main__'):
  main()
