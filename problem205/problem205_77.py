n,p = list(map(int,input().split())); s = [int(i) for i in input()]

ans = 0

if p == 2 or p == 5:
    for i in range(n):
        if s[i]%p == 0:
            ans += i+1
    print(ans)
    
else:
    s = s[::-1]
    res = [0] * p
    arr = [0] * n
    tmp = 0
    for i in range(n):
        tmp += s[i]*pow(10,i,p)
        tmp %= p
        arr[i] = tmp
    for i in arr:
        res[i] += 1
    for i in res:
        ans += i*(i-1)
    ans //= 2
    ans += res[0]
        
    print(ans)