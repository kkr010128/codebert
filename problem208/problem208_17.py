n,m=map(int,input().split())
l=[]
for i in range(m):
    order=list(map(int,input().split()))
    l.append(order)

if n==1:
    for i in range(10):
        if all(str(i)[l[j][0]-1]==str(l[j][1]) for j in range(m)):
            print(i)
            exit()
elif n==2:
    for i in range(10,10**2):
        if all(str(i)[l[j][0]-1]==str(l[j][1]) for j in range(m)):
            print(i)
            exit()
else:
    for i in range(10**2,10**3):
        if all(str(i)[l[j][0]-1]==str(l[j][1]) for j in range(m)):
            print(i)
            exit()
print(-1)