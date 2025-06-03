n=int(input())#ｎはデータセットの数
for i in range(n):#ｎ回繰り返す
  edge=input().split()#入力
  edge=[int(j) for j in edge]#入力
  edge.sort()#ここでedge[2]が最大になる
  if(edge[0]**2+edge[1]**2==edge[2]**2):#直角三角形かどうか
    print("YES")
  else:#そうでないなら
    print("NO")