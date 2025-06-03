def cin():  return list(map(int,input().split()))

a, b, c = cin()
res1 = 4 * a * b
res2 = (c - a - b) ** 2
if c - a - b <= 0:  print("No")
else:
    if res1 < res2:  print("Yes")
    else:  print("No")