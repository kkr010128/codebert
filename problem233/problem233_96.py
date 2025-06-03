n=int(input());p=list(map(int,input().split()))
count=0;m=n+1
for i in p:
  if m>i: m=i;count+=1
print(count)