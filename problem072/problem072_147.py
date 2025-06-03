# サイコロを振る回数
count = int(input())
# ゾロ目の回数
zorome = 0

for i in range(0, count):
  dice1, dice2 = input().split()

  # ゾロ目が3回で連続たらループ抜ける
  if zorome == 3:
    break

  if dice1 == dice2:
    zorome += 1
  else:
    zorome = 0
  
if zorome == 3:
  print("Yes")
else:
  print("No")
