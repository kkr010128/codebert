import sys
H, N = map(int, input().split())
data = [int(i) for i in input().split()]
DATA = sorted(data, reverse=True)
count = 0
 
for i in range(N):
  H = H - DATA[i]
  if H <= 0:
    print("Yes")
    sys.exit()
else:
  print("No")