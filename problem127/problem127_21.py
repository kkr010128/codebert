X, Y = list(map(int, input().split()))
judge = 0
for a in range(X + 1):
  if (Y - a*2 - (X-a)*4 ) == 0:
    print("Yes")
    judge = 1
    break
if judge == 0:
  print("No")