h,w,k=map(int,input().split())
board=[list(input()) for _ in range(h)]
acum=[[0]*w for _ in range(h)]

def count(x1,y1,x2,y2): #事前に求めた2次元累積和を用いて左上の点が(x1,y1)、右下の点(x2,y2)の長方形に含まれる1の個数を数える
  ret=acum[y2][x2]
  if x1!=0:
    ret-=acum[y2][x1-1]
  if y1!=0:
    ret-=acum[y1-1][x2]
  if x1!=0 and y1!=0:
    ret+=acum[y1-1][x1-1]
  return ret

for i in range(h): #2次元累積和により左上の点が(0,0)、右下の点が(j,i)の長方形に含まれる1の個数を数える
  for j in range(w):
    if board[i][j] == '1':
      acum[i][j]+=1
    if i!=0:
      acum[i][j]+=acum[i-1][j]
    if j!=0:
      acum[i][j]+=acum[i][j-1]
    if i!=0 and j!=0:
      acum[i][j]-=acum[i-1][j-1]

ans = 10**18
for i in range(2**(h-1)):
  cnt = 0
  list = []
  flag = format(i,'b')[::-1] # '1'と'10'と'100'の区別のために必要
  #print(flag)
  for j in range(len(flag)):
    if flag[j] == '1': # ''をつける！
      cnt += 1
      list.append(j)
  list.append(h-1)
  #print(list)
  x1 = 0
  for x2 in range(w-1): #x1(最初は0)とx1+1の間からx=w-1とx=wの間までの区切り方をそれぞれ確かめる
    y1 = 0
    for y2 in list: #長方形のブロックの右下の点のy座標の候補をすべて試す
      if count(x1,y1,x2,y2) > k: #ある横の区切り方の下で、どのように縦を区切ってもブロックに含まれる1の個数がKより大きくなるとき、条件を満たす切り分け方は存在しない
        cnt += 10**18
      if count(x1,y1,x2,y2) <= k and count(x1,y1,x2+1,y2) > k: #ある位置でブロックを区切ると1の個数がK以下になるが、区切る位置を1つ進めると1の個数がKより大きくなるとき、その位置で区切る必要がある
        cnt += 1
        x1 = x2+1 #ある位置x2で区切ったとき、次からはx2+1を長方形のブロックの左上の点のx座標として見ればよい
        break
      y1 = y2+1 #(いま見ているブロックの右下の点のy座標)+1が次に見るブロックの左上の点のy座標に等しくなる
  y1 = 0
  for y2 in list:
    if count(x1,y1,w-1,y2) > k: #最後に縦で区切った位置以降で、あるブロックに含まれる1の個数がKより大きくなるとき、条件を満たすような区切り方は存在しない
      cnt += 10**18
      break
    y1 = y2+1
  ans = min(ans,cnt)
print(ans)