def f(num,l):
    k=0
    p=[0 for i in range(len(l))]
    for i in range(len(l)):
        if k>-1:
            p[i]=num
            if l[i]=='#':
                num+=1
                k=-1
        else:
            if l[i]!='#':
                p[i]=p[i-1]
            else:
                p[i]=num
                num+=1
    return p,num
h,w,k=map(int,input().split())
j=0
num=1
p=[[0 for i in range(w)] for i in range(h)]
for i in range(h):
    l=list(input())
    if j>-1:
        if '#' not in l:
            j+=1
        else:
            p[i],num=f(num,l)
            for k in range(j):
                p[k]=p[i]
            j=-1
    else:
        if '#' not in l:
            p[i]=p[i-1]
        else:
            p[i],num=f(num,l)
for i in range(h):
    print(*p[i])