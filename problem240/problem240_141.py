import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def main():
    n, m = [int(i) for i in input().strip().split()]
    accepted = [False] * (n + 1)
    WA_cnt = [0] * (n + 1)
    for _ in range(m):
        p, s = input().strip().split()
        p = int(p)
        if accepted[p]:
            continue
        else:
            if s == "AC":
                accepted[p] = True
            elif s == "WA":
                WA_cnt[p] += 1
    ac = 0
    wa = 0
    for res, cnt in zip(accepted, WA_cnt):
        if res:
            ac += 1
            wa += cnt

    print(ac, wa)

    return


if __name__ == "__main__":
    main()
