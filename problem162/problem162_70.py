n, m = map(int,input().split())

if n%2 == 1:
    for i in range(m):
        print(n//2-i,n//2+i+1)
else:
    ni = 1
    l = 1
    r = n
    while ni <= n//4 and ni <= m:
        print(l,r)
        l += 1
        r -= 1
        ni += 1
    r -= 1
    while ni <= m:
        print(l,r)
        l += 1
        r -= 1
        ni += 1
