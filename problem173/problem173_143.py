n=int(input())

lfb=[]
l=[]

for i in range(1,n+1):
    if i%3==0:
        lfb.append(i)
    elif i%5==0:
        lfb.append(i)
    elif i%15==0:
        lfb.append(i)
    else:
        l.append(i)
print(sum(l))


