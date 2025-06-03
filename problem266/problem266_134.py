X = int(input())
menu = [100,101,102,103,104,105]

ans = 0
x = X//100

X_bit2 = int(str(X)[-2:])
if X_bit2 <= x*5:
  ans = 1

print(ans)