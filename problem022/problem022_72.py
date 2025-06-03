tmp=input()
a=input().split()
tmp=input()
b=input().split()
c=0
for i in b:
    if i in a:
        c+=1
print(c)
