n=int(input())
l0=[[] for _ in range(n)]
l1=[[] for _ in range(n)]
for i in range(n):
    a=int(input())
    for j in range(a):
        x,y=map(int,input().split())
        if y==0:
            l0[i].append(x)
        else:
            l1[i].append(x)
ans=0
for i in range(2**n):
    s0=set()
    s1=set()
    num=0
    num1=[]
    num0=[]
    for j in range(n):
        if (i>>j) & 1:
            num1.append(j+1)
            for k in range(len(l0[j])):
                s0.add(l0[j][k])
            for k in range(len(l1[j])):
                s1.add(l1[j][k])
        else:
            num0.append(j+1)
    for j in range(len(s1)):
        if s1.pop() in num0:
            num=1
            break
    if num==0:
        for j in range(len(s0)):
            if s0.pop() in num1:
                num=1
                break
    if num==0:
        ans=max(ans,len(num1))
print(ans)
