n=int(input())
a=[int(i) for i in input().split()]

c=1000

for i in range(n-1):
    if a[i]<a[i+1]:
        c += (c//a[i])*(a[i+1]-a[i])
print(c)