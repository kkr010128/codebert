x,n=map(int,input().split())
p=set(map(int,input().split()))

low=x
high=x
while True:
  if low not in p:
    print(low)
    break
  elif high not in p:
    print(high)
    break
  low-=1
  high+=1