from sys import stdin
input = stdin.readline


def main():
  N = int(input())

  if N % 2:
    print(0)
    return

  nz = 0
  i = 1
  while True:
    if N//(5**i)//2 > 0:
      nz += (N//(5**i)//2)
      i += 1
    else:
      break

  print(nz)


if(__name__ == '__main__'):
  main()
