import sys
def input():
    return sys.stdin.readline()[:-1]
n,k = map(int,input().split())
a = list(map(int,input().split()))
f = list(map(int,input().split()))
l = -1
r = 10**12

a.sort(reverse=True)
f.sort()

while l+1<r:
    #print()
    now = (l+r)//2
    s=0
    for i in range(n):
        s += max(0,a[i]-now//f[i])
    if s<=k:
        r=now
    else:
        l=now

print(r)
