def resolve():
    N = int(input())
    print(1000 * ((1000 + (N-1)) // 1000) - N)
resolve()