k = int(input())
a, b=map(int, input().split())

c=0
for i in range(a, b+1):
  if i%k == 0:
    c += 1
  else:
    pass    
if c == 0:
  print("NG")
else:
  print("OK")