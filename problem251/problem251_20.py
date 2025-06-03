from sys import stdin
input = stdin.readline


def main():
  N, K = list(map(int, input().split()))
  R, S, P = list(map(int, input().split()))
  T = input()[:-1]

  mem = []
  hand_map = {'r': 'p', 's': 'r', 'p': 's'}
  score_map = {'r': P, 's': R, 'p': S}

  score = 0

  for i in range(K):
    mem.append(hand_map[T[i]])
    score += score_map[T[i]]

  for i in range(K, N):
    if not mem[i-K] == hand_map[T[i]]:
      mem.append(hand_map[T[i]])
      score += score_map[T[i]]
      continue
    cand = ['r', 's', 'p']
    # print(mem[i-K])
    cand.remove(mem[i-K])
    if i+K < N and not(mem[i-K] == hand_map[T[i+K]]):
      cand.remove(hand_map[T[i+K]])
    mem.append(cand[0])

  print(score)


if(__name__ == '__main__'):
  main()
