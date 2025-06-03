N, M = [int(n) for n in input().split(" ")]

def comb(n):
    if n <= 1:
        return 0
    return n * (n - 1) // 2

print(comb(N) + comb(M))