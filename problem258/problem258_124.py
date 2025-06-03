import sys
n=int(input())
if n%2:
  print(0)
  sys.exit()
# 10->50->2500の個数
cnt=0
v=10
while 1:
  cnt+=n//v
  if n//v==0:
    break
  v*=5
print(cnt)