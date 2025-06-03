from sys import stdin
input = stdin.readline


def rec(H):
  if H == 1:
    return 1
  # print(H)
  return 1 + 2*rec(int(H/2))


def main():
  H = int(input())

  print(rec(H))


if(__name__ == '__main__'):
  main()
