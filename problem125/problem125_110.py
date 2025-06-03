cnt=0
radi=0
x=int(input())
while True:
  cnt+=1
  radi+=x
  radi%=360
  if radi==0:
    print(cnt)
    break