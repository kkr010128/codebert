line = list(map(int, input().split()))

kyori = line[0]
lim = line[1]
speed = line[2]

ans = kyori/speed

if ans <= lim:
  print("Yes")

else:
  print("No")