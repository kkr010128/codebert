from sys import stdin
input = stdin.readline


def check(min_, max_, x):
  if x < min_:
    return 0
  else:
    return int((min(max_, x) - min_)/10) + 1


def main():
  N = int(input())

  if len(str(N)) == 1:
    print(N)
    return
  sum_ = 0
  for l in range(1, 10):
    for r in range(l, 10):
      temp = sum_
      min_ = int(str(l) + '0'*(len(str(N))-2) + str(r))
      max_ = int(str(l) + '9'*(len(str(N))-2) + str(r))
      A = check(min_, max_, N)
      # max_ = int(str(l) + '9'*(len(str(N))-3) + str(r))
      for gap in range(len(str(N))-2):
        A += (10**gap)

      min_ = int(str(r) + '0'*(len(str(N))-2) + str(l))
      max_ = int(str(r) + '9'*(len(str(N))-2) + str(l))
      B = check(min_, max_, N)
      for gap in range(len(str(N))-2):
        B += (10**gap)

      if l == r:
        A += 1
        B += 1
        sum_ += A*B
      else:
        sum_ += 2*A*B
      # print(l, r, sum_ - temp)

  print(sum_)


if(__name__ == '__main__'):
  main()
