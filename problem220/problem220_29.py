a = input().split()
b = list(map(int, input().split()))
c = input()
if a[0]==c:
  print(b[0]-1, b[1])
else:
  print(b[0], b[1]-1)