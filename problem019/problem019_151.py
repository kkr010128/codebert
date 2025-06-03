n,q=map(int,input().split())
Q=[]
sum=0
for i in range(n):
    tmp=input().split()
    tmp[1]=int(tmp[1])
    Q.append(tmp[0])
    Q.append(tmp[1])

loop=0
while loop==0:
    for i in range(len(Q)//2):
        tmp=[Q[0],Q[1]]
        if tmp[1]>q:
            sum+=q
            Q.append(tmp[0])
            Q.append(tmp[1]-q)
        else:
            sum+=tmp[1]
            print(tmp[0],sum)
        Q.pop(0)
        Q.pop(0)
    if len(Q)==0:
        break

