from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  A = sorted(list(map(int, input().split())))

  not_divisible = [False]*(10**6+1)
  for i in range(N):
    not_divisible[A[i]] = True

  prev = 0
  for i in range(N):
    if not_divisible[A[i]]:
      j = A[i] + A[i]
      while j <= A[-1]:
        not_divisible[j] = False
        j += A[i]
    if prev == A[i]:
      not_divisible[A[i]] = False
    prev = A[i]

  cnt = 0
  for i in range(N):
    if not_divisible[A[i]]:
      cnt += 1

  print(cnt)


if(__name__ == '__main__'):
  main()
