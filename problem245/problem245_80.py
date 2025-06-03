N = int(input())
a = list(input())
count=0
for i in range(N):
  if a[i] == 'A' and i<len(a)-2:
    if a[i+1]=='B' :
      if a[i+2]=='C':
        count+=1
        
print(count)