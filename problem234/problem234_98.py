N=int(input())

D={(x//10,x%10):0 for x in range(100)}
for i in range(1,N+1):
    if i<10:
        D[(i,i)]=1
    else:
        Q=int(str(i)[0])
        R=i%10
        D[(Q,R)]+=1

S=0
for x in range(1,10):
    for y in range(1,10):
        S+=D[(x,y)]*D[(y,x)]

print(S)
