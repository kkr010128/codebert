def resolve():
    import math
    n, m = list(map(int, input().split()))

    ans1 = math.factorial(n) // (math.factorial(n-2) * 2) if n > 1 else 0
    ans2 = math.factorial(m) // (math.factorial(m-2) * 2) if m > 1 else 0
    print(ans1 + ans2)
resolve()