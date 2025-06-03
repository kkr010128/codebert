n,k,s=map(int,input().split())
a=[s]*k
b=[3]*(n-k)+[s]*k
p=max(s//2-1,1)
for i in range(n-k):
    if i%p==0:
        a.append(s-1)
    else:
        a.append(2)
if s!=2 and s!=1:
    print(*a)
else:
    print(*b)