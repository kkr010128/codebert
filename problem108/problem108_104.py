def resolve():
    N = int(input())
    ans = N % 1000
    if ans == 0:
        print(0)
    else:
        print(1000 - ans)
resolve()