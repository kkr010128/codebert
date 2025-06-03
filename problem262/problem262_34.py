n=int(input())
l=[]
lis=[]
for _ in range(n):
    a=int(input())
    l.append(a)

    li=[]
    for _ in range(a):
        c,d=map(int,input().split())
        li.append([c,d])
    lis.append(li)

ans=-1
for i in range(2**n-1,-1,-1):
    mark=bin(i)[2:]
    mark=(n-len(mark))*'0'+mark
    s=0
    record=[-1]*n
    f=1
    for j in range(n):
        for k in range(l[j]):
            number=lis[j][k][0]-1
            hou=lis[j][k][1]
            if int(mark[j])==1:
                if record[number]==-1:
                    record[number]=hou
                elif record[number]!=hou:f=0
            if f==0:break
        if f == 0: break

    if f==1:
        F=True
        for i in range(n):
            if record[i]!=-1:
                if record[i]!=int(mark[i]):
                    F=False
                    break
        if F==True:
            print(mark.count('1'))
            exit()












