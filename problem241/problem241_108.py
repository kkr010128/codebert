import itertools
from collections import deque
from sys import stdin
input = stdin.readline


def main():
  H, W = list(map(int, input().split()))

  M = [input()[:-1] for _ in range(H)]

  def bfs(start):
    dist = [[float('inf')]*W for _ in range(H)]
    dist[start[0]][start[1]] = 0

    is_visited = [[0]*W for _ in range(H)]
    is_visited[start[0]][start[1]] = 1

    q = deque([start])
    max_ = 0

    while len(q):
      now_h, now_w = q.popleft()
      if M[now_h][now_w] == '#':
        return
      for next_h, next_w in ((now_h+1, now_w),
                             (now_h-1, now_w),
                             (now_h, now_w-1),
                             (now_h, now_w+1)):

        if not(0 <= next_h < H) or not(0 <= next_w < W) or \
           (is_visited[next_h][next_w] == 1) or \
           M[next_h][next_w] == '#':
           # (dist[next_h][next_w] != float('inf')) or \
          continue

        dist[next_h][next_w] = dist[now_h][now_w] + 1
        is_visited[next_h][next_w] = 1

        max_ = max(max_, dist[next_h][next_w])
        q.append((next_h, next_w))
    return max_

  max_ = 0
  for h in range(H):
    for w in range(W):
      if M[h][w] == '.':
        max_ = max(bfs((h, w)), max_)

  print(max_)


if(__name__ == '__main__'):
  main()
