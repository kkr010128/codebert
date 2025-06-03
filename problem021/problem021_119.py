s=0
j=0
a=[]
k=[]
l=[]
for i,x in enumerate(input()):
    if x=='\\':
        a+=[i]
    elif x=='/' and a:
        j=a.pop()
        y=i-j;s+=y
        while k and k[-1]>j:
            y+=l.pop()
            k.pop()
        k+=[j]
        l+=[y]
print(s)
print(len(k),*(l))
