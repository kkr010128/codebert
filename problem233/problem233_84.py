n=int(input())
p=list(map(int,input().split()))

a=n
c=0

for i in p:
    if i<=a:
        a=i
        c+=1
print(c)