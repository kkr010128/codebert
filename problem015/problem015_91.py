n = int(raw_input())
a = map(int,raw_input().split(' '))

nswap=0
for i in range(n):
    min_v = a[i]
    min_p = i
    for j in range(i,n):
        if min_v > a[j]:
            min_v = a[j]
            min_p = j
    if min_p != i:
        a[i],a[min_p]=a[min_p],a[i]
        nswap+=1

print ' '.join([str(v) for v in a])
print nswap