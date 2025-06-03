n = int(input())
a = input().strip().split()
#Bubble sort
b = a[:]
for i in range(n):
    for j in range(n-1,i,-1):
        if b[j][1] < b[j-1][1]:
            b[j],b[j-1] = b[j-1],b[j]
print(' '.join(b))
print('Stable')
#Selection sort
for i in range(n):
    minj = i
    for j in range(i,n):
        if a[j][1] < a[minj][1]:
            minj = j
    a[i],a[minj] = a[minj],a[i]
print(' '.join(a))
print('Stable' if b == a else 'Not stable')