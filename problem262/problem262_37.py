n = int(input())

testimony = []

for i in range(n):
    a = int(input())
    test = []
    for j in range(a):
        x,y = map(int,input().split())
        test.append([x-1,y])
    testimony.append(test)

ans = 0

for i in range(2**n):
    good = [0]*n
    f = 1
    for j in range(n):
        if (i>>j)&1:
            good[j] = 1

    for k in range(n):
        if good[k]:
            for l,m in testimony[k]:
                if good[l] != m:
                    f = 0
    
    if f:
        ans = max(ans,sum(good))

print(ans)