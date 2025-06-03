H,W,K=map(int,input().split())

smat=[[1 if x=="#" else 0 for x in input()] for _ in range(H)]
#print(smat)

answer_mat=[[0]*W for _ in range(H)]
cnt=1
lastrow_exist=-1
for i in range(H):
  row_num=sum(smat[i])
  if row_num==0:
    continue
  elif row_num==1:
    for j in range(W):
      for ii in range(lastrow_exist+1,i+1):
        answer_mat[ii][j]=cnt
    cnt+=1
    lastrow_exist=i
  else:
    berry_list=[0]*W
    isFirst=True
    for j in range(W):
      if smat[i][j]==1:
        if not isFirst:
          cnt+=1
        else:
          isFirst=False
      berry_list[j]=cnt
    
    for j in range(W):
      for ii in range(lastrow_exist+1,i+1):
        answer_mat[ii][j]=berry_list[j]
        
    cnt+=1
    lastrow_exist=i
        
if lastrow_exist<H-1:  
  for j in range(W):
    for ii in range(lastrow_exist+1,H):
      answer_mat[ii][j]=answer_mat[lastrow_exist][j]
      
for i in range(H):
  print(*answer_mat[i])