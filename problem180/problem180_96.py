from sys import stdin
input = stdin.readline


def main():
  N, K = list(map(int, input().split()))

  surp = N % K
  print(min(surp, abs(surp-K)))


if(__name__ == '__main__'):
  main()
