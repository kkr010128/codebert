NUM = list(map(int,input().split()))

if(NUM[0] > NUM[1]):
  print("safe")
elif(NUM[0] <= NUM[1]):
  print("unsafe")
