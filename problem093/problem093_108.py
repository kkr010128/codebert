N, K = map(int, input().split())
moves = [0] + list(map(int, input().split()))
points = [0] + list(map(int, input().split()))
INF = 10**10

arrived = [0 for _ in range(N+1)]
answer = -INF
for move in range(1, N+1):
  if arrived[move] == 1:
    continue
  else:
    arrived[move] = 1
    komas = [move]
    next = moves[move]
    while(arrived[next] == 0):
      arrived[next] = 1
      komas.append(next)
      next = moves[next]
    len_k = len(komas)
    sum_k = [0 for _ in range(len_k*2)]
    sum_k[0] = points[komas[0]]
    for i in range(1, len_k*2):
      sum_k[i] = sum_k[i-1] + points[komas[i%len_k]]
    scores = [-INF for _ in range(len_k+1)]
    for j in range(len_k):
      for k in range(1, len_k+1):
        scores[k] = max(scores[k], sum_k[j+k] - sum_k[j])
    if K > len_k and scores[len_k] > 0:
      max_s = -INF
      max_k = -INF
      for m in range(1, len_k+1):
        if m <= K%len_k:
          max_k = max(max_k, scores[m])
        max_s = max(max_s, scores[m])
      answer = max(answer, max_k+scores[len_k]*(K//len_k), max_s+scores[len_k]*(K//len_k-1))
    else:
      max_s = -INF
      for m in range(1, min(K, len_k)+1):
        max_s = max(max_s, scores[m])
      answer = max(answer, max_s)
print(answer)