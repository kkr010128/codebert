n = int(input())
if n%2:
    print(0)
else:
    ans = 0
    for i in range(1,100):
        ans += (n//(5**i*2))
        if n < 5**i:
            break
    print(ans)