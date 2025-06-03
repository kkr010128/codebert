from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  A = list(map(int, input().split()))

  order = sorted(range(1, N+1), key=lambda i: A[i-1])

  print(*order, sep=' ')


if(__name__ == '__main__'):
  main()
