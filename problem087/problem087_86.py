N=str(input())
NN=0
for i in range(len(N)):
    NN=NN+int(N[i])
  
if NN%9==0:print('Yes')
else:print('No')