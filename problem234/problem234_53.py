A= int(input())
l=[[0]*10 for _ in range(10)]
for i in range(1,A+1):
   n=str(i)
   if n[0] == "0" or n[-1] == "0":
      continue
   l[int(n[0])][int(n[-1])]+=1
ans=0
for i in range(1,10):
   for j in range(1,10):
      ans+=l[i][j] * l[j][i]
print(ans)