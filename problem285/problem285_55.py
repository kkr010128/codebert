s=str(input())
s=list(s)
temp=[]
cnt=0
ans=0
for i in range(len(s)):
  if s[i]=="<":
    if i!=0 and s[i-1]==">":
      temp.append(cnt)
      cnt=0
    cnt=cnt+1
  else:
    if i!=0 and s[i-1]=="<":
      temp.append(cnt)
      cnt=0
    cnt=cnt+1
temp.append(cnt)
if s[0]=="<":
  for i in range(0,len(temp)-1,2):
    tempmin=min(temp[i],temp[i+1])-1
    tempmax=max(temp[i],temp[i+1])
    temp[i]=tempmin
    temp[i+1]=tempmax
else:
  for i in range(1,len(temp)-1,2):
    tempmin=min(temp[i],temp[i+1])-1
    tempmax=max(temp[i],temp[i+1])
    temp[i]=tempmin
    temp[i+1]=tempmax
for i in range(len(temp)):
  ans=ans+temp[i]*(temp[i]+1)//2
print(ans)