def d(x):
    dl=[]
    for i in range(1, int(x**0.5)+1):
        if x%i==0:
            dl.append(i)
            if i!=x//i:
                dl.append(x//i)
    return dl

n=int(input())
ans=0
t=d(n)
for i in t:
    if i==1:
        continue
    tn=n
    while tn>=i:
        if tn%i==0:
            tn//=i
        else:
            tn%=i
    if tn==1:
        ans+=1
ans+=len(d(n-1))-1
print(ans)