n,k=list(map(int, input("").split()))
d=[]
a=[]
t=[]
for i in range(k):
    d.append(int(input()))
    a.append(list(map(int, input("").split())))
for i in range(n):
    t.append(True)
for i in range(k):
    for j in a[i]:
        if t[j-1]:
            t[j-1]=False
out=0
for i in t:
    if i:
        out+=1
print(out)
