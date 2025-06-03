a,b=[int(i) for i  in input().split()]
c=max(a,b)
if(a<=b):
    d=a
else:
    d=b
for i in range(1,100001):
    if((d*i)%c==0):
        print(d*i)
        break
