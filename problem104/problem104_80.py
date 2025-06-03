m,n,p = map(int, input().split())
l=[]
for i in range(m,n+1):
    if i % p == 0:
        l.append(i)
print(len(l))