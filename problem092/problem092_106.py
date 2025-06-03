import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


def main():
    x, k, d = map(int, input().split())
    desired = abs(x) // d
    if k <= desired:
        if x < 0:
            x += k * d
        else:
            x -= k * d
        print(abs(x))
        return
    if x < 0:
        x += desired * d
    else:
        x -= desired * d
    if (k - desired) % 2 == 0:
        print(abs(x))
        return
    if x == 0:
        print(d)
    elif x > 0:
        x -= d
        print(abs(x))
    elif x < 0:
        x += d
        print(abs(x))


if __name__ == '__main__':
    main()