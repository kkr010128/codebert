A1=list(map(int,input().split()))
A2=list(map(int,input().split()))
A3=list(map(int,input().split()))
n = int(input())
B = [int(input()) for i in range(n)]
A = [A1,A2,A3]
ans = [[0,0,0],[0,0,0],[0,0,0]]
for b in B:
  for i in range(3):
    for j in range(3):
      if A[i][j] == b:
        ans[i][j] = 1
for i in range(3):
  if ans[i][0] and ans[i][1] and ans[i][2]:
    print("Yes")
    quit()
  if ans[0][i] and ans[1][i] and ans[2][i]:
    print("Yes")
    quit()
if ans[0][0] and ans[1][1] and ans[2][2]:
  print("Yes")
  quit()
if ans[0][2] and ans[1][1] and ans[2][0]:
  print("Yes")
  quit()
print("No")