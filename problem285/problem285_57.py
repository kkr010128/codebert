from sys import stdin
input = stdin.readline


def main():
  S = input()[:-1]

  N = len(S)+1

  from_left = [0]*N
  from_right = [0]*N

  for i, s in enumerate(S, 1):
    if s == '>':
      from_left[i] = 0
    else:
      from_left[i] = from_left[i-1]+1

  for i, s in enumerate(S[::-1]):
    i = N-2-i
    if s == '<':
      from_right[i] = 0
    else:
      from_right[i] = from_right[i+1]+1

  seq = [x if x>y else y for x, y in zip(from_left, from_right)]

  answer = sum(seq)
  print(answer)


if(__name__ == '__main__'):
  main()
