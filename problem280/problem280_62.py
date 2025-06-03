#!/usr/bin/env python3

import math

def solver(visited, coord, depth = 0):
  dists = []

  if len(visited) == depth:
    for i in range(1, len(visited)):
      x1, y1 = coord[visited[i - 1]][0], coord[visited[i - 1]][1]
      x2, y2 = coord[visited[i]][0], coord[visited[i]][1]
      dists.append(math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)))
    return sum(dists)

  for i in range(0, len(visited)):
    if visited[i] != -1: continue
    visited[i] = depth
    dists.append(solver(visited, coord, depth + 1))
    visited[i] = -1;

  return sum(dists)

def main():
  n = int(input())
  coord = []
  for i in range(0, n):
    coord.append([int(c) for c in input().split()])

  print(solver([-1 for i in range(0, n)], coord) / math.factorial(n))

if __name__ == "__main__":
  main()

