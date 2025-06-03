from collections import defaultdict
from itertools import product
 
H,W,K = map(int,input().split())
S = [input() for i in range(H)]
 
C = [[int(S[i][k]) for i in range(H)] for k in range(W)]
answer = H*W #出力がこれを超えることはない
for X in product([False,True],repeat = H-1):
  M = [[0]]
  ans = sum(X)
  if ans > answer:#初期値がanswerよりも大きかったら考える必要がない
    continue
  for i,x in enumerate(X):#配列Mの作成
    if x:
      M.append([])
    M[-1].append(i+1)
  D = [0]*len(M)
  for c in C:
    for k,m in enumerate(M):
      D[k] += sum(c[i] for i in m)#k番目の要素に足していく
      #Dにどんどん代入することによってどの列まで足すことができるか算出することができる
    if any(d>K for d in D):#一つでもKを超えていたら
      ans += 1
      if ans >answer:
        break
      D = [sum(c[i] for i in m) for m in M]#超えた行について再び調査
      if any(d>K for d in D):
        ans = answer + 1
        #デフォルトanswerの結果より高い値にしてこの結果が出力にならないように設定する
        break
  answer = min(answer,ans)#あるXに対してanswerを算出(更新)
print(answer)