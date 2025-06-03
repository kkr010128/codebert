import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)

MOD = 10 ** 9 + 7


def main():
    N = int(input())
    A = list(map(int, input().split()))
    RGB = [1, 0, 0]
    ans = 1
    if A[0] !=0:
        print(0)
        return
    for i in range(1, N):
        a = A[i]
        if a == 0:
            if 0 in RGB:
                j = RGB.index(a)
                RGB[j] += 1
            else:
                print(0)
                return
        elif a not in RGB:
            print(0)
            return
        else:
            k = RGB.count(a)
            ans *= k
            ans %= MOD
            j = RGB.index(a)
            RGB[j] += 1
    z = RGB.count(0)
    if z == 0:
        ans *= 6
        ans %= MOD
    elif z == 1:
        ans *= 6
        ans %= MOD
    else:
        ans *= 3
        ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()
