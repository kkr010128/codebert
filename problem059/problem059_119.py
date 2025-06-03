r,c=list(map(int,input().split()))
s=[0 for i in range(c+1)]

for i in range(r):
    l=list(map(int,input().split()))
    l.append(sum(l))
    print(' '.join(map(str,l)))
    s=[s[i]+l[i] for i in range(c+1)]
print(' '.join(map(str,s)))