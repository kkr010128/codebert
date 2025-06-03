n=int(input())

a=[None] * (n+1)
a[0] = 1
a[1] = 1

for i in range(n-1):
    a[i+2]=a[i]+a[i+1]

print(a[n])

