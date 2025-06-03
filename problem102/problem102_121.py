N, K = list(map(int, input().split(' ')))

marks = list(map(int, input().split(' ')))

for i in range(N-K):
  if marks[i] < marks[K+i]:
    print('Yes')
  else:
    print('No')