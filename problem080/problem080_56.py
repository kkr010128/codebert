n=int(input())
a=[]
b=[]
c=[]
d=[]
for i in range(n):
    k,l=map(int,input().split())
    a.append((k-l,i))
    b.append((k+l,i))
    c.append((-k-l,i))
    d.append((-k+l,i))
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
d.sort(reverse=True)
print(max(a[0][0]+d[0][0],b[0][0]+c[0][0]))