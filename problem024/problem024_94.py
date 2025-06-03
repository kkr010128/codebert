n, k = map(int, input().split())
#n=num of lagage
#k=num of trucks
a = []

#import sys
#input = sys.stdin.readline

a = [int(input()) for _ in range(n)]

def isOk(mx):
    num_t = 0
    t = 0
    for i in range(n):
        if a[i]>mx:
            return False
        t += a[i]
        if t>mx:
            t = a[i]
            num_t += 1
            if num_t == k:
                return False
    return True

l = sum(a)//k - 1
r = sum(a)

while l<r:
    m = (l+r)//2
    if isOk(m):
        r = m 
    else:
        m += 1
        l = m

print(m)
