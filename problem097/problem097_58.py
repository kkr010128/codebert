def resolve():
    k = int(input())
    x = 7 % k
    for i in range(1, k + 1):
        if x == 0:
            print(i)
            return
        x = (x * 10 + 7) % k

    print(-1)

resolve()