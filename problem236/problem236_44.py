def a_painting():
    from math import ceil
    H = int(input())
    W = int(input())
    N = int(input())
    return ceil(N / max(H, W))

print(a_painting())