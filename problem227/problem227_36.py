from sys import stdin
input = stdin.readline


def main():
  N, K = list(map(int, input().split()))
  H = list(map(int, input().split()))
  H = sorted(H)

  if K == 0:
    print(sum(H))
    return
  print(sum(H[:-K]))


if(__name__ == '__main__'):
  main()
