d = {}
m = [[False]*3 for _ in range(3)]
for i in range(3):
  for j, val in enumerate(list(map(int,input().split()))):
    d[val] = (i,j)
    
N = int(input())

for _ in range(N):
  key = int(input())
  if key in d:
    i,j = d[key]
    m[i][j] = True
  
def main():
  if m[0][0] and m[1][1] and m[2][2]:
    return True
  if m[0][2] and m[1][1] and m[2][0]:
    return True
  for i in range(3):
    if m[i][0] and m[i][1] and m[i][2]:
      return True
    if m[0][i] and m[1][i] and m[2][i]:
      return True
      
  return False

ans = main()
if ans:
  print("Yes")
else:
  print("No")