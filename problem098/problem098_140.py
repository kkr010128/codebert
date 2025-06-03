n=int(input())
s=input()
r=0
for i in s:
  if(i=="R"):
    r+=1
ans=0
for j in range(r):
  if(s[j]=="W"):
    ans+=1
print(ans)