X,Y = map(int,input().split())

turtle_leg = 4
crane_leg = 2

for i in range(X+1):
  if Y == turtle_leg*i+crane_leg*(X-i):
    print ("Yes")
    break
  if i==X:
    print ("No")
    break