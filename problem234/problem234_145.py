n=int(input())
d=[10*[0]for _ in range(10)]
for i in range(1,n+1):d[int(str(i)[0])][int(str(i)[-1])]+=1
ans=0
for i in range(1,10):
  for j in range(1,10):ans+=d[i][j]*d[j][i]
print(ans)