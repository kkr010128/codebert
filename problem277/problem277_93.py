# ある行について、
# 最初のイチゴが出てから、次のイチゴの手前までを一つの番号とする
# それ以降は、次のイチゴが出る手前までを次の番号とする
# イチゴがない行があったら、となりの行の結果をコピーする

import sys
readline = sys.stdin.readline

H,W,K = map(int,readline().split())
A = [readline().rstrip() for i in range(H)]
ans = [[0] * W for i in range(H)]
exist_straw = [True] * H
num = 0 # 次の番号
for i in range(H):
  # イチゴがない行はいったん後回し
  if "#" not in A[i]:
    exist_straw[i] = False
    continue
  num += 1
  # イチゴが出たらnumを1増やしてから更新　ただし最初のイチゴは無視
  first = True
  for j in range(W):
    if A[i][j] == "#":
      if first:
        first = False
      else:
        num += 1
    ans[i][j] = num

# 行を上から順に見て、ある行にはイチゴが存在して、次の行には存在しない場合、行をコピーする
# それを逆順も実行すると全ての行が埋まる

for i in range(H - 1):
  if exist_straw[i] and not exist_straw[i + 1]:
    ans[i + 1] = ans[i]
    exist_straw[i + 1] = True

for i in range(H - 1,0,-1):
  if exist_straw[i] and not exist_straw[i - 1]:
    ans[i - 1] = ans[i]
    exist_straw[i - 1] = True
    
for a in ans:
  print(*a)