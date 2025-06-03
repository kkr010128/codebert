n=int(input())
n=n-1
a=[]
q=n//26
r=n%26
a.insert(0,r)
while q>=26:
    q=q-1
    r=q%26
    a.insert(0,r)
    q=q//26
a.insert(0,q-1)
b=[]
for i in range(len(a)):
    x=int(a[i])
    if x<0:
        x=0
    else:
        x=chr(x+97)
        b.append(x)
c="".join(b)
print(c)