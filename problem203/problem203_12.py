a,b = map(int,input().split())

for i in range(1,100000):
  x = i*8
  y = i*10
  if x//100 == a and y//100 == b:
    print(i)
    exit()
print(-1)