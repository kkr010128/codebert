n=int(input())
a=list(map(int,input().split()))

cnt=[0]*(10**5+1)

for i in a:
  cnt[i]+=1

xxx=sum(a)

q=int(input())

for i in range(q):
  l,r=map(int,input().split())
  pin=cnt[l]
  cnt[r]+=pin
  cnt[l]=0

  xxx+=(r-l)*pin

  print(xxx)