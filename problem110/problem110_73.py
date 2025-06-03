import itertools


def main():
    # n = int(input())
    h, w, k = map(int, input().split())
    # a = list(map(int, input().split()))
    # s = input()
    c = []
    for i in range(h):
        c.append(list(input()))

    total = 0
    for i in list(itertools.chain.from_iterable(c)):
        if i == "#":
            total += 1

    ans = 0
    for i in range(2**h):
        for j in range(2**w):
            count = 0
            for ii in range(h):
                for jj in range(w):
                    if (i >> ii & 1 or j >> jj & 1) and c[ii][jj] == "#":
                        count += 1
            if total - count == k:
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
