import sys

def main():
  n, x, y = map(int, sys.stdin.buffer.readline().split())
  L = [0] * n
  for i in range(1, n):
    for j in range(i + 1, n + 1):
      d = j - i
      if i <= x and y <= j:
        d -= y - x - 1
      elif i <= x and x < j < y:
        d = min(d, x - i + y - j + 1)
      elif x < i < y and y <= j:
        d = min(d, i - x + j - y + 1)
      elif x < i and j < y:
        d = min(d, i - x + y - j + 1)
      L[d] += 1
  for a in L[1:]:
    print(a)

main()