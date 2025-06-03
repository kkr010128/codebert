n=int(input())
ans=[]
for i in range(55000):
  if int(i*1.08)==n:
    ans.append(i)
if ans==[]:
  print(':(')
else:
  print(ans[0])