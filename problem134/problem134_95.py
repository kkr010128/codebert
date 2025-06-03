n = int(input())
a = list(map(int, input().split()))

try:
    idx = a.index(0)
    print(0)

except ValueError:

    ans = a[0]
    for i in range(1, len(a)):
        ans *= a[i]
        if ans > 10**18:
            print('-1')
            exit()

    print(ans)