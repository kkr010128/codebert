from sys import stdin
input = stdin.readline


def main():
  N, M = list(map(int, input().split()))
  s = []
  c = []
  for i in range(M):
    ss, cc = map(int, input().split())
    s.append(ss)
    c.append(cc)

  # print(10**(N-1), 10**N)
  # print(s, c)
  if N == 1:
    left = 0
  else:
    left = 10**(N-1)
  for i in range(left, 10**N):
    flag = True
    for j in range(M):
      if str(i)[s[j]-1] != str(c[j]):
        flag = False
    if flag:
      print(i)
      return

  print(-1)


if(__name__ == '__main__'):
  main()
