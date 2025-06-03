n = int(input())
a = list(map(int, input().split()))
p = 1000
k = 0
for i in range(n-1):
    if k>0 and a[i]>a[i+1]:
        p += k*a[i]
        k = 0
    elif k==0 and a[i]<a[i+1]:
        k = p//a[i]
        p %= a[i]
if k>0:
    p += k*a[-1]
print(p)