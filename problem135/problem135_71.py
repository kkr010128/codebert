def main(istr, ostr):
  x, y = istr.readline().strip().split()
  a = int(x)
  b0, _, b1, b2 = y
  b0, b1, b2 = list(map(int, [b0, b1, b2]))

  c = a * (100 * b0 + 10 * b1 + b2)
  res = c // 100
  print(res, file=ostr)


if __name__ == "__main__":
  import sys

  main(sys.stdin, sys.stdout)
