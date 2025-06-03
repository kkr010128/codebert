n,d = map(int,input().split())
l=[]
for _ in range(n):
    x,y=map(int,input().split())
    l.append(((x**2)+(y**2))**(0.5))
l.sort()
c=0
for i in l:
    if i>d:
        break
    else:
        c+=1
print(c)