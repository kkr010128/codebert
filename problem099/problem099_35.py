#最大値の最小値を求める問題は二分探索
#求めるものを変数と見て丸太の最大値がxだとすると
#丸太の長さは全てx以下である必要があるため切るべき回数がわかる
#それがk回以下ならokだしそれがk回を超えていたらだめ
n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
ng=0
ok=max(a)

def check(x):
  num=0
  for i in range(n):
    if a[i]%x==0:
      num=num+a[i]//x-1
    else:
      num=num+a[i]//x
  return num<=k

while ok-ng>1:
  mid=(ok+ng)//2
  if check(mid):
    ok=mid
  else:
    ng=mid
print(ok)

