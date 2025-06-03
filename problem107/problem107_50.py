N = int(input())
X = input()
memo = {}
X_int = int(X, 2)


def popcount(n: int):
    x = bin(n)[2:]
    return x.count("1")


pcf = popcount(int(X, 2))
pcm = pcf - 1
pcp = pcf + 1
xm = X_int % pcm if pcm != 0 else 0
xp = X_int % pcp


def f(n: int, ops: int):

    while n != 0:
        n %= popcount(n)
        ops += 1
    return ops


def rev(x: str, i: int):
    if x == "1":
        if pcm == 0:
            return -1
        n = (xm - (pow(2, N-i-1, pcm))) % pcm
    else:
        n = (xp + (pow(2, N-i-1, pcp))) % pcp
    return n


if __name__ == "__main__":
    for i, x in enumerate(X):
        n = rev(x, i)
        if n == -1:
            print(0)
        else:
            print(f(n, 1))
