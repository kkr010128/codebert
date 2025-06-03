k = int(input())

if(k%2 == 0 or k%5 == 0):
    print('-1')
else:
    if(k%7 == 0):
        k = k // 7
    num = 1
    ans = 1
    while(True):
        if(num%k == 0):
            print(ans)
            break
        else:
            num %= k
            num *= 10
            num += 1
            ans += 1


