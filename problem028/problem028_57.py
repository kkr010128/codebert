def f(num):
    mn = 20000
    for y in c:
        if y > num/2:
            break
        mn = min(mn, yen[y]+yen[num-y])
    return mn

n, m = map(int, input().split())
c = list(map(int, input().split()))
c = sorted(c)
yen = [0 for i in range(n+1)]
yen[1] = 1
for num in range(2, n+1):
    if num in c:
        yen[num] = 1
    else:
        yen[num] = min(yen[num-1]+1,f(num))

print(yen[n])
