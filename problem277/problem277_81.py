from collections import deque

H, W, K=map(int, input().split())
cake=[input() for _ in range(H)]
rows_list=[]
upper=0
for i in range(H):
  for j in range(W):
    if cake[i][j]=="#":
      rows_list.append([upper, i])
      upper=i+1
      break
rows_list[-1][-1]=H-1
ans_list=[]
for rows in rows_list:
  for i in range(rows[0], rows[1]+1):
    left=0
    for j in range(W):
      if cake[i][j]=="#":
        ans_list.append([rows[0], rows[1], left, j])
        left=j+1
    if ans_list:
      ans_list[-1][-1]=W-1
ans=[[0 for _ in range(W)] for _ in range(H)]
key=1
for l in ans_list:
  for i in range(l[0], l[1]+1):
    for j in range(l[2], l[3]+1):
      ans[i][j]=key
  key+=1
for a in ans:
  print(*a)