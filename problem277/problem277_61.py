H,W,s=list(map(int,input().split()))
l=[list(input()) for i in range(H)]
l_h=[0]*H
for i in range(H):
   if "#" in set(l[i]):
      l_h[i]=1
cnt=0
bor=sum(l_h)-1
for i in range(H):
   if cnt==bor:
      break
   if l_h[i]==1:
      l_h[i]=-1
      cnt+=1
cnt=1
import numpy as np
tmp=[]
st=0
ans=np.zeros((H,W))
for i in range(H):
   tmp.append(l[i])
   if l_h[i]==-1:
      n_tmp=np.array(tmp)
      s_count=np.count_nonzero(n_tmp=="#")-1
      for j in range(W):
         ans[st:i+1,j]=cnt
         if "#" in n_tmp[:,j] and s_count>0:
            cnt+=1
            s_count-=1
      st=i+1
      cnt+=1
      tmp=[]
n_tmp=np.array(tmp)
s_count=np.count_nonzero(n_tmp=="#")-1
for j in range(W):
   ans[st:i+1,j]=cnt
   if "#" in n_tmp[:,j] and s_count>0:
      cnt+=1
      s_count-=1
for i in ans:
   print(*list(map(int,i)))