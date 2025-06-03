import sys
from collections import deque

def main():
  h, w = map(int, input().split())
  area = [[s for s in sys.stdin.readline().strip()] for _ in range(h)]
  start_point = {0:set(), 1:set(), 2:set(), 3:set(), 4:set()}
  min_neighbor = 4
  for i in range(h):
    for j in range(w):
      if area[i][j] == '#':
        continue
      roads = 0
      if i > 0 and area[i - 1][j] == '.':
        roads += 1
      if i < h - 1 and area[i + 1][j] == '.':
        roads += 1
      if j > 0 and area[i][j - 1] == '.':
        roads += 1
      if j < w - 1 and area[i][j + 1] == '.':
        roads += 1
      min_neighbor = min(min_neighbor, roads)
      start_point[roads].add((i, j))
  max_cost = 0
  for start in start_point[min_neighbor]:
    queue = deque()
    queue.append(start)
    cost = 0
    visited = set()
    while len(queue) > 0:
      roads = len(queue)
      found = False
      for i in range(roads):
        s = queue.popleft()
        if s in visited:
          continue
        found = True
        visited.add(s)
        i = s[0]
        j = s[1]
        if i > 0 and area[i - 1][j] == '.':
          queue.append((i - 1, j))
        if i < h - 1 and area[i + 1][j] == '.':
          queue.append((i + 1, j))
        if j > 0 and area[i][j - 1] == '.':
          queue.append((i, j - 1))
        if j < w - 1 and area[i][j + 1] == '.':
          queue.append((i, j + 1))
      if not found:
        cost -= 1
      max_cost = max(cost, max_cost)
      if found:
        cost += 1
  print(max_cost)

if __name__ == '__main__':
  main()