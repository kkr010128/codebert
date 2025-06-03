s=input()
t=input()
lent=len(t)
num=lent
ls=[]
count=0

for i in range(len(s)-lent+1):
  st=s[i:i+num]
  num+=1
  
  for j in range(lent):
    if st[j]!=t[j]:
      count+=1
      
  ls.append(count)
  count=0
  
print(min(ls))