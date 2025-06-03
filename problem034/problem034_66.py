dice = list(map(int,input().split()))


kaisuu = int(input())

lastlist = []
frlist = []
for i in range(kaisuu):
  up,front = list(map(int,input().split()))
  if up == dice[0] :
    frlist = [1,2,4,3,1]
  if up == dice[1]:
    frlist = [0,3,5,2,0]
  if up == dice[2]:
    frlist = [0,1,5,4,0]
  if up == dice[3]:
    frlist = [0,4,5,1,0]
  if up == dice[4]:
    frlist = [0,2,5,3,0]
  if up == dice[5] :
    frlist = [1,3,4,2,1]
 
  k = dice.index(int(front))
  for n in frlist[0:4] :
    if n == k :
      l = frlist.index(int(n))
      m = l + 1
  lastlist.append(dice[frlist[m]])
for g in lastlist :
  print(g)
      
