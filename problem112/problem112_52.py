n,k=map(int,input().split())
a=list(map(int,input().split()))
mod=10**9+7

if n==k:
  # n==kなら全部選ぶ必要がある
  ans=1
  for q in a:
    ans*=q
    ans%=mod
  print(ans)
  exit()
  
if all(q>=0 for q in a):
  # 全部正なら大きい方から
  ans=1
  a.sort()
  for _ in range(k):
    ans*=a.pop()
    ans%=mod
  print(ans)
  exit()

if all(q<0 for q in a):
  # 全部負なら
  # kが奇数の時は大きい方(絶対値が小さい方)から
  # kが偶数のときは小さい方(絶対値が大きい方)から
  ans=1
  a.sort()
  if k%2==0:
    for i in range(k):
      ans*=a[i]
      ans%=mod
  else:
    for _ in range(k):
      ans*=a.pop()
      ans%=mod
  print(ans)
  exit()
  
pos=[]
neg=[]
for q in a:
  if q>=0:
    pos.append(q)
  else:
    neg.append(q)

pos.sort()
neg.sort()
neg=neg[::-1]
# arr[-1]の絶対値が最大となるようにソート

kk=k
# kが奇数のときは、posの最大は絶対とって良い
if kk%2==1:
  ans=pos.pop()%mod
  kk=kk-1
else:
  ans=1

# 2個ずつ比較しながら掛け算
# 片方の長さが2に満たない場合は、もうそちらからは取らない
while kk>0:
  if len(pos)<2:
    ans=ans*neg.pop()%mod*neg.pop()%mod
    kk-=2
  elif len(neg)<2:
    ans=ans*pos.pop()%mod*pos.pop()%mod
    kk-=2
  else:
    if pos[-1]*pos[-2]>=neg[-1]*neg[-2]:
      ans=ans*pos.pop()%mod*pos.pop()%mod
      kk-=2
    else:
      ans=ans*neg.pop()%mod*neg.pop()%mod
      kk-=2
      
print(ans)
