#Breadth First Search
n=int(input())
V=[]
a=[1]
for i in range(n):
    V.append([int(i) for i in input().split()])
    a.append(0)
V=sorted(V,key=lambda x:x[0])
print('1 0')
d=1
c=0
w=[0]
p=[]
while c<n and w!=[]:
    i=0
    y=[]
 #   print(c)
    while c<n and i<len(w):
        j=2
        while j<2+V[w[i]][1] and c<n:
            if a[V[w[i]][j]-1]==0:
        #        print(a)
                a[V[w[i]][j]-1]=1
                p.append([V[w[i]][j],d])
                c+=1
                y.append(V[w[i]][j]-1)
            j+=1
        i+=1
    w=y
    d+=1
p=sorted(p, key=lambda x:x[0])
#print(p)
i=2
j=0
while i <=n and j<len(p):
    while p[j][0]>i:
        print(str(i) +" -1")
        i+=1
    print(str(p[j][0])+" "+str(p[j][1]))
    i+=1
    j+=1
while i<=n:
    print(str(i)+" -1")
    i+=1