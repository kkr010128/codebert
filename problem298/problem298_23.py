n,k=(int(x) for x in input().split())
h=list(int(x) for x in input().split())
c=0
for i in h:
    if i>=k:
        c+=1

print(c)