def mapt(fn, *args):
    return tuple(map(fn, *args))


def main():
    n, m = mapt(int, input().split(" "))
    h = mapt(int, input().split(" "))
    ok = [True for i in range(n)]
    for i in range(m):
        a, b = mapt(int, input().split(" "))
        a = a-1
        b = b-1
        if h[a] <= h[b]: ok[a] = False
        if h[b] <= h[a]: ok[b] = False

    print(sum(ok))

main()