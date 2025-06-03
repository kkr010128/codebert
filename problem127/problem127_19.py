X,Y = (int(x) for x in input().split())
crane = 0
turtle = 0

for i in range(X+1):
  crane = (i)
  turtle = X-crane

  if crane*2 + turtle*4 == Y:
    print('Yes')
    break
  elif i == X:
    print('No')