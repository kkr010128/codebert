n = int(input())

if n % 2 == 1:
    print(0)
elif n % 2 == 0:
    ans = 0
    k = 10
    while n >= k:
        ans += n//k
        k *= 5
        
    print(ans)