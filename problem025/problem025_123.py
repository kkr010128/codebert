n=int(input())
a=list(map(int,input().split()))
q=int(input())
m=list(map(int,input().split()))

d={}
for i in range(2**n):
    c=0
    for j in range(n):
        if (i>>j)&1:
            c+=a[j]
    d[c]=1

for i in range(q):
    if m[i] in d:
        print("yes")
    else:
        print("no")
