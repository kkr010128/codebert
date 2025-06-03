n=int(input())
a=list(map(int,input().split()))
q=int(input())
m=list(map(int,input().split()))
l=[]
for i in range(2**n):
    sub=0
    for j in range(n):
        if (i>>j)&1==1:
            sub+=a[j]
    l.append(sub)
for i in m:
    if i in l:
        print("yes")
    else:
        print("no")
