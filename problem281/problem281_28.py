X, Y = [int(x) for x in input().split()]
M = 10**9+7
if (X + Y) % 3:
  print(0)
else:
  x = X - (X+Y)//3
  y = Y - (X+Y)//3
  if x < 0 or y < 0:
    print(0)
  else:
    #print(x, y)
    #x+y c x
    #(x+y)!/x!/y!
    ans = 1
    for j in range(y):
      #print(j)
      #print(x+j+1, j+1)
      ans *= (x+j+1) * pow(j+1, -1, M)
      ans %= M
    print(ans)