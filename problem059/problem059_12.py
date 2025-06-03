r,c=map(int, input().split())
total=[0]*(c+1)
for i in range(r):
    a=list(map(int, input().split()))
    a.append(sum(a))
    print(*a)
    for j in range(c+1):
        total[j]+=a[j]
print(*total)
