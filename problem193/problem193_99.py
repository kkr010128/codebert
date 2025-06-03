import re

H,W,K = map(int,input().split())
grid = [[0 for i in range(W+1)]]
for i in range(H):
  S = input()
  grid.append([0]+[ int(S[i]) for i in range(W) ])

#累積和gridの作成
#行について
for i in range(H+1):
  for j in range(W):
    grid[i][j+1] += grid[i][j]
#列について
for j in range(W+1):
  for i in range(H):
    grid[i+1][j] += grid[i][j]   

min_cnt = (H-1)*(W-1)
#横の区切りを作る
for h in range(2**(H-1)):
  cnt = 0
  #二進数の文字列を取得
  bin_str = format(h,"0{}b".format(H-1)) 
  #区切りのインデックスリスト
  l_p =[1]+[ x.start()+2 for x in re.finditer("1",bin_str) ] +[H+1]

  #cntに区切りの分だけ付け加える
  cnt = cnt + len(l_p) - 2
  
  ws = 0
  for w in range(1,W+1):
    for k in range(len(l_p)-1):
      if grid[l_p[k+1]-1][w]-grid[l_p[k+1]-1][w-1] > K:
        min_cnt=(H-1)*(W-1)+1
      if grid[l_p[k+1]-1][w]- (grid[l_p[k]-1][w]+grid[l_p[k+1]-1][ws]-grid[l_p[k]-1][ws]) > K:
        cnt = cnt + 1
        ws = w-1
        break    
  min_cnt = min(min_cnt,cnt)

###
print(min_cnt)        