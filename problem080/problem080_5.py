n=int(input())
x=[0]*n
y=[0]*n
z=[]
w=[]
for i in range(n):
    x[i],y[i]= list(map(int, input().strip().split()))
    z.append(x[i]+y[i])
    w.append(x[i]-y[i])
a=max(z)-min(z)
b=max(w)-min(w)
print(max(a,b))