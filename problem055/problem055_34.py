n = int(input())
home = [[0 for i in range(20)] for j in range(15)]  #横最大20→間の#,縦最大3階*4棟+3行の空行
for i in range(n) :
  b, f, r, v = map(int, input().split())
  h = (b - 1) * 4 + f - 1
  w = r * 2 - 1
  s = v
  home[h][w] += s
for y in range(15) :
  for x in range(20) :
    if(y % 4 == 3) :
      home[y][x] = "#"
    elif(x % 2 == 0) :
      home[y][x] = " "
    print(home[y][x], end = "")
  print() 
