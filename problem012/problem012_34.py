n=int(input())
c=0
for _ in range(n):
 x=int(input())
 if 2 in [x,pow(2,x,x)]:c+=1
print(c)
