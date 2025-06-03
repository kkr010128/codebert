K = int(input())

ans = 1
num = 0
seven = 7

if not K%2:
    print(-1)
else:
    for i in range(K):
        num = num + seven
        seven = seven*10%K
        num = num%K
        if num == 0:
            print(ans)
            break
        ans += 1
    else:
        print(-1)