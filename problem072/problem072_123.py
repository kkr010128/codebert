roop_num = int(input())

xy = [map(int, input().split()) for _ in range(roop_num)]
x, y = [list(i) for i in zip(*xy)]

z_counter = 0
flg = False

for i in range(roop_num):
  if(x[i] == y[i]):
    z_counter = z_counter +1
  else:
    z_counter = 0
  if(z_counter == 3):
    flg = True
    break

if(flg):
  print("Yes")
else:
  print("No")
