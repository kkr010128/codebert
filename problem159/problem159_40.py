x = int(input())

b = 100
for i in range(1,10**18):
  b += b//100
  if b >= x:
    print(i)
    break