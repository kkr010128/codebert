import sys
N,M=map(int,input().split())
slist=list(map(int,input()))

seq=0
for s in slist:
  if s==0:
    seq=0
  else:
    seq+=1
    if seq==M:
      print(-1)
      sys.exit(0)

class SegTree:
  #init(init_val, ide_ele): 配列init_valで初期化 O(N)
  def __init__(self, init_val, segfunc, ide_ele):
    #init_val: 配列の初期値
    #segfunc: 区間にしたい操作
    #ide_ele: 単位元
    #n: 要素数
    #num: n以上の最小の2のべき乗
    #tree: セグメント木(1-index)
    n = len(init_val)
    self.segfunc = segfunc
    self.ide_ele = ide_ele
    self.num = 1 << (n - 1).bit_length()
    self.tree = [ide_ele] * 2 * self.num
    # 配列の値を葉にセット
    for i in range(n):
      self.tree[self.num + i] = init_val[i]
    # 構築していく
    for i in range(self.num - 1, 0, -1):
      self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

  #update(k, x): k番目の値をxに更新 O(logN)      
  def update(self, k, x):
    #k番目の値をxに更新
    #k: index(0-index)
    #x: update value
    k += self.num
    self.tree[k] = x
    while k > 1:
      self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
      k >>= 1

  #query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
  def query(self, l, r):
    #[l, r)のsegfuncしたものを得る
    #l: index(0-index)
    #r: index(0-index)
    res = self.ide_ele
    l += self.num
    r += self.num
    while l < r:
      if l & 1:
        res = self.segfunc(res, self.tree[l])
        l += 1
      if r & 1:
        res = self.segfunc(res, self.tree[r - 1])
      l >>= 1
      r >>= 1
    return res

#segfunc
def segfunc(x,y):
  return min(x,y) #最小値
#ide_ele
ide_ele=float("inf") #最小値
#init
seg=SegTree([float("inf")]*(N+1), segfunc, ide_ele)

dist_list=[float("inf")]*(N+1)
seg.update(N,0)
dist_list[N]=0
for i in reversed(range(N)):
  if slist[i]==0:
    left=i+1
    right=min(i+M,N)
    dist=seg.query(left,right+1)+1
    seg.update(i,dist)
    dist_list[i]=dist

answer_list=[]
i=0
while i<N:
  for j in range(1,M+1):
    if dist_list[i]>dist_list[i+j]:
      answer_list.append(j)
      i+=j
      break
    
print(*answer_list)