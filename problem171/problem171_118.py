#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
  N = int(input())
  A = [(i, v) for i, v in enumerate(map(int, input().split()))]
  values = [[0] * (N + 1) for _ in range(N + 1)]

  A.sort(key=lambda x:-x[1])

  for i, (p, v) in enumerate(A):
    for j in range(i + 1):
      left = abs((p - j) * v)
      right = abs((N - 1 - (i - j) - p) * v)

      values[i + 1][j + 1] = max(values[i][j] + left, values[i + 1][j + 1])
      values[i + 1][j] = max(values[i][j] + right, values[i + 1][j])

  print(max(values[-1]))


if __name__ == '__main__':
  main()
