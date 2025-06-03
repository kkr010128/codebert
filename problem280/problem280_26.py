n=int(input())
x,y=[],[]
for i in range(n):
    x1,y1=map(int,input().split())
    x.append(x1)
    y.append(y1)
s=0
for i in range(n):
    for j in range(n):
        if i!=j:
            s+=((x[i]-x[j])**2+(y[i]-y[j])**2)**(1/2)
print(s/n)