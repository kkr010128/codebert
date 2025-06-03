List = []
for i in range (3):
  List.append(list(map(int, input().split())))
Row = int(input())
Ball = []
for i in range (Row):
  Ball.append(int(input()))
for x in range(Row):
  for i in range(3):
    for j in range(3):
      if Ball[x] == List[i][j]:
        List[i][j] = 0
if List[0][0] == 0 and List[0][1] == 0 and List[0][2] == 0:
  print("Yes")
elif List[1][0] == 0 and List[1][1] == 0 and List[1][2] == 0:
  print("Yes")
elif List[2][0] == 0 and List[2][1] == 0 and List[2][2] == 0:
  print("Yes")
elif List[0][0] == 0 and List[1][0] == 0 and List[2][0] == 0:
  print("Yes")
elif List[0][1] == 0 and List[1][1] == 0 and List[2][1] == 0:
  print("Yes")
elif List[0][2] == 0 and List[1][2] == 0 and List[2][2] == 0:
  print("Yes")
elif List[0][0] == 0 and List[1][1] == 0 and List[2][2] == 0:
  print("Yes")
elif List[0][2] == 0 and List[1][1] == 0 and List[2][0] == 0:
  print("Yes")
else:
  print("No")