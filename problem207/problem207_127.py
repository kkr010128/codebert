map_list = [list(map(int,input().split())) for x in range(3)]
 
n = int(input())
for i in range(n):
  a = int(input())
  for i in range(3):
    for j in range(3):
      if map_list[i][j] == a:
        map_list[i][j] = 0

ans = "No"
for k in range(3):
  if map_list[0][k] == map_list[1][k] == map_list[2][k] or \
     map_list[k][0] == map_list[k][1] == map_list[k][2]:
      ans = "Yes"
      break
  if map_list[0][0] == map_list[1][1] == map_list[2][2] or \
	 map_list[0][2] == map_list[1][1] == map_list[2][0]:
      ans = "Yes"
print(ans)