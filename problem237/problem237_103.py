from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  X_L = [list(map(int, input().split())) for _ in range(N)]
  # print(N)

  X_L.sort(key=lambda x: x[0]+x[1])
  # print(X_L)

  def min_robots(X_L):
    # print(X_L)
    N = len(X_L)
    added = [0]
    for i in range(1, N):
      pre = added[-1]
      if X_L[pre][0] + X_L[pre][1] <= X_L[i][0] - X_L[i][1]:
        added.append(i)
    return len(added)

  print(min_robots(X_L))


if(__name__ == '__main__'):
  main()