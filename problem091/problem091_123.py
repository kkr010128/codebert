#abc175b
n=int(input())
l=list(map(int,input().split()))
l.sort()
cnt=0
for i in range(n):
 for j in range(i):
  for k in range(j):
   if l[k]!=l[j] and l[i]!=l[j] and l[k]+l[j]>l[i]:
    cnt+=1
print(cnt)
