x=int(input())
for i in range(1001):
  for j in range(100*i,105*i+1):
    if x==j:
      print(1)
      exit(0)
print(0)