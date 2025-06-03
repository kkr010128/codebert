from sys import stdin
input = stdin.readline


def main():
  A, B = input().split()
  A = int(A)
  # B = int(100*float(B))
  B = int(B[0]+B[2:])

  # print((A*B)//100)
  if A*B < 100:
    print(0)
  else:
    print(str(A*B)[:-2])


if(__name__ == '__main__'):
  main()
