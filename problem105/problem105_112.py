n=int(input())
a=list(map(int,input().split()))
c=0
for i in a[::2]:
  if i%2!=0:
    c+=1
print(c)