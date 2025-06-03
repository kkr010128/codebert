n=int(input())
p=list(map(int,input().split()))
minnumber=1e9
count=0

for i in p:
  if i<=minnumber:
    count+=1
    minnumber=i
    
print(count)