n = int(input())
a = list(map(int,input().split()))
x = 1
if 0 in a:
  print(0)
  exit()
for e in a:
  x *= e
  if x > 10**18:
    print(-1)
    exit()
print(x)
