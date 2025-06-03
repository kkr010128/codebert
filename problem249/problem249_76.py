a, b, k = map(int, input().split())
if k >= a + b:
  print("0 0")
elif k >= a:
  print("0" + " " + str(b - (k-a)))
else:
  print(str(a-k) + " " + str(b))
  
