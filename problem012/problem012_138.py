n=int(input())
c=0
for _ in range(n):
 x=int(input())
 if x==2:c+=1
 elif pow(2,x-1,x)==1:c+=1
print(c)
