
n,k = map(int,input().split())
a = list(map(int,input().split()))

l=0
r=10**9

def check(x):
    now = 0
    for i in range(n):
        now += (a[i] - 1 )// x
    return now <= k

while r-l > 1:
    x = (l+r) //2
    if check(x):
        r = x
    else:
        l = x

print(r)

