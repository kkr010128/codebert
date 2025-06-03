def resolve():
    import math
    n = int(input())
    for i in range(1, n+1):
        if math.floor(i * 1.08) == n:
            print(i)
            quit()
    print(":(")
resolve()