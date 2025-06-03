N=int(input())
stones = list(input())
l = 0
r = N-1
count = 0

while(True):
  while(stones[l] == "R" and l < N-1):
    l += 1
  while(stones[r] == "W" and r > 0):
    r -= 1
  if (l >= r):
    print(count)
    exit()
  else:
    count += 1
    l += 1
    r -= 1