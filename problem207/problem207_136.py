seen = [0,0,0,0,0,0,0,0,0]
seen[0],seen[1],seen[2] = (map(int,input().split()))
seen[3],seen[4],seen[5] = (map(int,input().split()))
seen[6],seen[7],seen[8] = (map(int,input().split()))
over = "No"
N = int(input())
for x in range(N):
  num = int(input())
  if num in seen:
    seen[seen.index(num)] = "O"
if seen[0] == "O":
  if seen[1] == "O" and seen[2] == "O":
    over = "Yes"
  if seen[3] == "O" and seen[6] == "O":
    over = "Yes"
  if seen[4] == "O" and seen[8] == "O":
    over = "Yes"
if seen[8] == "O":
  if seen[6] == "O" and seen[7] == "O":
    over = "Yes"
  if seen[2] == "O" and seen[5] == "O":
    over = "Yes"
if seen[4] == "O":
  if seen[6] == "O" and seen[2] == "O":
    over = "Yes"
  if seen[1] == "O" and seen[7] == "O":
    over = "Yes"
  if seen[3] == "O" and seen[5] == "O":
    over = "Yes"
print(over)