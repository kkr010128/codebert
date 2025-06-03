h, n = map(int, input().split())
aa = [int(a) for a in input().split()]

all = sum(aa)

if h <= all :
  print("Yes")
else :
  print("No")