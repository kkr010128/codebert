n=int(input())
c=input()
a=0
i=0
j=len(c)-1
while(i<j):
  while(c[i]=="R" and i<j):
      i+=1
  while(c[j]=="W" and i<j):
      j-=1
  if i<j:
    a+=1
    i+=1
    j-=1
print(a)  