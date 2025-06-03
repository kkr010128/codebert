n = int(input())

A = [[] for i in range(n)]

for i in range(n):
  A[i] = list(map(int, input().split()))

B = [[0 for i in range(2)] for j in range(n)]
order = []

time = 0

def dfs(n, num):
  global time
  while time < 2*n:
    a = num
    time += 1
    if B[num-1][0] == 0: # まだ発見していないとき
      if A[num-1][1] != 0: # 次の頂点があるとき
        order.append(A[num-1][0]) # 発見したことを記録する
        B[num-1][0] = time # 発見時刻を記録する
        A[num-1][1] -= 1 # 次の頂点数を１減らす
        if B[A[num-1][2]-1][0] == 0: # 次の頂点がまだ発見されていないとき
          num = A[num-1].pop(2) # 次の頂点に移動
        else: # 次の頂点が発見済みのとき
          del A[num-1][2] # 次の頂点をルートから削除
      else: # 次の頂点がないとき
        l = len(order) # これまで経由した頂点数
        order.append(A[num-1][0]) # 発見したことを記録する
        order.append(A[num-1][0]) # 調べ終えたことを記録する
        B[num-1][0] = time # 発見時刻を記録する
        time += 1 # 時刻を１進める
        B[num-1][1] = time # 調査終了時刻を記録する
        num = order[l-1] # １つ前の頂点に戻る
    elif  B[num-1][1] == 0: # 発見しているが、調べ終えていないとき
      if A[num-1][1] == 0: # 次の頂点がないとき
        order.append(A[num-1][0]) # 調べ終えたことを記録する
        B[num-1][1] = time # 調査終了時刻を記録する
        m = order.index(num) # 発見した順番を調べる
        num = order[m-1] # 発見する前の頂点に移動
      else: # 次の頂点があるとき
        A[num-1][1] -= 1 # 次の頂点数を１減らす
        order.append(A[num-1][0]) # 経由したことを記録する
        if B[A[num-1][2]-1][0] == 0: # 次の頂点がまだ発見されていないとき
          num = A[num-1].pop(2) # 次の頂点に移動
        else: # 次の頂点が発見済みのとき
          del A[num-1][2] # つぎの頂点をルートから削除
        time -= 1 # 時刻を戻す
    else: # すでに調査終了した頂点に移動したとき
      l = len(order) # これまで経由した頂点数
      num = order[l-1] # １つ前の頂点に戻る
      time -= 1 # 時刻を戻す
      if num == a:
        break

for i in range(n):
  if B[i][0] == 0:
    dfs(n, A[i][0])

for i in range(n):
  print(str(i+1) + " ", end="")
  print(" ".join(map(str, B[i])))
