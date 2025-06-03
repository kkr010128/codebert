H, A = (int(x) for x in input().split())

if H%A==0:
  print(int(H/A))
else:
  print(int(H/A)+1)

