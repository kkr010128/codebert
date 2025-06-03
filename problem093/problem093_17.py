# -*- coding: utf-8 -*-
N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
k_max = 10100
score = [-10**18-1] * N

for i in range(N):
  score_i = [-10**18-1] * k_max # iからスタートしてK回操作する場合の累積和
  score_i[0] = C[P[i]-1]
  index = P[i]-1
  for k in range(1, K):
    if index == i:
      # 既に進んだことがあるマスの場合
      
      loop_score = score_i[k-1] # 1ループで増えるスコア
      if loop_score > 0:
        loop_num = k # ループする要素数はk(indexが0 ~ k-1)
        
        tmp_score = [-10**18-1] * k_max
        tmp_score[0] = (K//k -1) * loop_score
#        print("loop_score", loop_score)
#        print("tmp_score", tmp_score)
        tmp_index = index
#        print("loop_num + K%k + 1", loop_num + K%k + 1)
        for j in range (1, loop_num + K%k + 1):
          tmp_score[j] = tmp_score[j-1] + C[P[tmp_index]-1]
          tmp_index = P[tmp_index]-1
#        print("max(tmp_score)", max(tmp_score))
        score_i[k] = max(tmp_score)
      break
    score_i[k] = score_i[k-1] + C[P[index]-1]
    index = P[index]-1
  score[i] = max(score_i)
print(max(score))