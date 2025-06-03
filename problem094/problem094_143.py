R, C, K = map(int, input().split())
score = [[0]*C for i in range(R)]

for i in range(K):
  r, c, v = map(int, input().split())
  score[r-1][c-1]+=v
  
ans0 = [[0]*C for i in range(R)]
ans1 = [[0]*C for i in range(R)]
ans2 = [[0]*C for i in range(R)]
ans3 = [[0]*C for i in range(R)]

ans1[0][0]=score[0][0]
ans2[0][0]=score[0][0]
ans3[0][0]=score[0][0]

for i in range(R):
  for j in range(C):
    if i>0:
      ans0[i][j]=max(ans0[i][j],ans3[i-1][j])
      ans1[i][j]=max(ans1[i][j],ans3[i-1][j]+score[i][j])
      ans2[i][j]=max(ans2[i][j],ans3[i-1][j]+score[i][j])
      ans3[i][j]=max(ans3[i][j],ans3[i-1][j]+score[i][j])
    if j>0:
      ans0[i][j]=max(ans0[i][j],ans0[i][j-1])
      ans1[i][j]=max(ans1[i][j],ans0[i][j-1]+score[i][j],ans1[i][j-1])
      ans2[i][j]=max(ans2[i][j],ans1[i][j-1]+score[i][j],ans2[i][j-1])
      ans3[i][j]=max(ans3[i][j],ans2[i][j-1]+score[i][j],ans3[i][j-1])

print(ans3[R-1][C-1])