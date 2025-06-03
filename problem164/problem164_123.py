MON = list(map(int,input().split()))
 
while 1:
  
  MON[2] = MON[2] - MON[1]
  if(MON[2] <= 0):
    print("Yes")
    break
 
  MON[0] = MON[0] - MON[3]
  if (MON[0] <= 0 ):
    print("No")
    break