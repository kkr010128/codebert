n, k = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))

A.sort()
F.sort(reverse=True)

def is_ok(x):
    c = 0
    for i in range(n):
        a = A[i]
        f = F[i]
        if a >= x//f:
            c += a-x//f
    if c <= k:
        return True
    else:
        return False

if is_ok(0):
    print(0)
    exit()

l = 0
r = 10**18
while l+1 < r:
    c = (l+r)//2
    if is_ok(c):
        r = c
    else:
        l = c
print(r)
