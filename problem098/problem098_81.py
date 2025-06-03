n = int(input())
s = input().rstrip()

i=0
j=n-1
c= 0

while i!=j:
  while s[j]!='R' and j>i:
    j-=1
    
  while s[i]=='R' and j>i:
    i+=1
 
  if i!=j:
    c+= 1
    i+= 1
    j-=1
  if i>=j:
    break
    
print(c)