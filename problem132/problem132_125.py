n,k=map(int, input().split())
a = list(map(int, input().split()))
k = min(k,50)
for i in range(k):
    aa = [0]*n
    for j in range(n):
        aa[max(0,j-a[j])] += 1
        if j+a[j]+1 < n: aa[j+a[j]+1] -= 1
    for j in range(n-1):aa[j+1] = aa[j]+aa[j+1]
    a = aa[:]

print(*a)