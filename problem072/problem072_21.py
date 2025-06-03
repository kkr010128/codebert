N = int(input())
D = [input().split() for i in range(N)]
cnt=0
for i in range(N):
  if D[i][0] == D[i][1]:
    cnt+=1
    if cnt == 3:
      print("Yes")
      exit()
  else:
    cnt=0
print("No")