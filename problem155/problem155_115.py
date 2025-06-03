n,m=list(map(int, input("").split()))
h=list(map(int, input("").split()))
o=[]
for i in range(n):
    o.append(1)
for i in range(m):
    a,b=list(map(int, input("").split()))
    if h[a-1] <=h[b-1]:
        o[a-1]=0
    if h[a-1] >=h[b-1]:
        o[b-1]=0
print(sum(o))