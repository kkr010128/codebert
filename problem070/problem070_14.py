#Union-Find木の実装
from collections import Counter
N,M=map(int,input().split())
 
#初期化
par=[i for i in range(N)]#親の要素(par[x]=xのときxは木の根)
rank=[0]*N#木の深さ
 
#木の根を求める
def find(x):
  #xが根だった場合xをそのまま返す
  if par[x] == x:
    return x
  else:
    #根が出るまで再帰する
    par[x] = find(par[x])
    return par[x]
 
#xとyの属する集合を併合
def unite(x,y):
  x=find(x)#xの根
  y=find(y)#yの根
  #根が同じなら何もしない
  if x == y:
    return
  #もし根の深さがyの方が深いなら
  if rank[x] < rank[y]:
    par[x] = y#yを根にする
  else:
    par[y] = x#xを根にする
    if rank[x] == rank[y]:
      rank[x]+=1
 
#xとyが同じ集合に属するか否か
#def same(x,y):
  #return find(x)==find(y)
 
for _ in range(M):
  a,b = map(int,input().split())
  a,b = a-1, b-1
  unite(a,b)
 
for i in range(N):
  find(i)
c=Counter(par)
print(len(c)-1)