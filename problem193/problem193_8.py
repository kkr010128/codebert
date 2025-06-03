from collections import defaultdict
from itertools import product
 
H, W, K = map(int, input().split())
S = [input() for _ in range(H)]
 
C = [[int(s[i]) for s in S] for i in range(W)]#列を一括りにする
 
total = sum(sum(c) for c in C)#すべての値の合計を算出
 
if total <= K:
  answer = 0
else:
  answer = H * W
  for X in product([False, True], repeat=H-1):#Hは行数
    #あるXについて一回目のfor文が回る
    ans = sum(X)#Trueの数を換算
    if ans > answer:
      continue
    M = [[0]]
    for i, x in enumerate(X):
      if x:#Trueなら実行
        M.append([])#Trueの数の配列が作成される
      M[-1].append(i+1)#一番最後にその番目をappendする
    D = [0] * len(M)#初期値を設定
    for c in C:
      for k, m in enumerate(M):
        D[k] += sum(c[i] for i in m)#k番目の要素に足していく
        #Dにどんどん代入することによってどの列まで足すことができるか算出することができる
      if any(d > K for d in D):#一つでもKを超えていたら
        ans += 1
        if ans > answer:
          break
        D = [sum(c[i] for i in m) for m in M]#Dの更新(1番最初のDに戻る)
        if any(d > K for d in D):#一つでもKを超えていたら
          ans = answer + 1#ansの更新
          break
    answer = min(answer, ans)

print(answer)