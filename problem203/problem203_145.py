import math
a,b=map(int,input().split())
count=1
while True:
  c=count*0.08
  d=count*0.1
  if math.floor(c)==a and math.floor(d)==b:
    print(count)
    break
  count+=1
  if count>1500:
    print(-1)
    break