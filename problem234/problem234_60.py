n = int(input())
# [1桁目][1の位]のリストを作る
ho = [[0 for nesya in range(9)] for motsu in range(9)]
for i in range(1,n+1):
  if i%10 != 0:
    a = str(i)
    #数字ごとにhoリストに足していく
    (ho[int(a[0])-1])[int(a[-1])-1] += 1
ans = 0
#1桁目と1の位が同じものに注意して組み合わせの数を計算する
for j in range(9):
  for k in range(j+1):
    if k == j:
      ans += (ho[k][k])**2
    else:
      ans += (ho[j][k])*(ho[k][j])*2
print(ans)