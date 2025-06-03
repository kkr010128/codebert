n=int(input())
l=list(map(int,input().split()))
ans=0
for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      num=[l[i],l[j],l[k]]
      if len(set(num))!=3:continue
      num.sort()
      if num[2]<num[1]+num[0]:ans+=1
print(ans)