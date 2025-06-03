s=input()
l=len(s)
l2=l//2
count=0
for i in range(l2):
  if s[i]!=s[l-1-i]:
    count+=1
print(count)